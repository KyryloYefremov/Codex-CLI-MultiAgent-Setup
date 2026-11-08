import sys
import json

def main():
    try:
        raw_payload = sys.stdin.read()
        event = json.loads(raw_payload)
    except Exception:
        sys.exit(0)

    subagent = event.get("subagent_name", "")
    
    # In SubagentStop, the output/result of the agent is in the payload
    output = event.get("output", {}).get("result", "").lower()

    if subagent == "reviewer":
        is_medium = "criticality: medium" in output or "criticality medium" in output
        is_high = "criticality: high" in output or "criticality high" in output
        verdict_pass = "verdict: pass" in output or "verdict pass" in output

        verdict_str = "PASS" if verdict_pass else "FAIL"

        if is_medium or is_high:
            print(f"\n────────────────── [ HITL GATEWAY: REVIEW ] ──────────────────", file=sys.stderr)
            print(f"Task Criticality: {'HIGH' if is_high else 'MEDIUM'}", file=sys.stderr)
            print(f"Reviewer Verdict: {verdict_str}", file=sys.stderr)
            print(f"──────────────────────────────────────────────────────────────", file=sys.stderr)
            
            choice = input("Do you approve the Reviewer's verdict to proceed? [y/N]: ").strip().lower()
            
            if choice != "y":
                response = {
                    "hookSpecificOutput": {
                        "permissionDecision": "deny",
                        "permissionDecisionReason": "Human operator manually overturned or rejected the Reviewer's verdict."
                    }
                }
                print(json.dumps(response))
                sys.exit(0)

    # Allow if Low Criticality, or if human approved
    response = {
        "hookSpecificOutput": {
            "permissionDecision": "allow"
        }
    }
    print(json.dumps(response))
    sys.exit(0)

if __name__ == "__main__":
    main()