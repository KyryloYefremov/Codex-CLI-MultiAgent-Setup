#!/usr/bin/env python3
import sys
import json

def main():
    try:
        raw_payload = sys.stdin.read()
        event = json.loads(raw_payload)
    except Exception:
        sys.exit(0)

    # Extract the prompt the CTO is sending to the Architect
    subagent = event.get("subagent_name", "")
    prompt = event.get("input", {}).get("prompt", "").lower()

    # Check if the task is flagged as High Criticality
    is_high_criticality = "criticality: high" in prompt or "criticality high" in prompt

    if subagent == "architect" and is_high_criticality:
        print(f"\n────────────────── [ HITL GATEWAY ] ──────────────────", file=sys.stderr)
        print(f"⚠️ HIGH CRITICALITY TASK DETECTED.", file=sys.stderr)
        print(f"The CTO is requesting to start the Architecture phase.", file=sys.stderr)
        print(f"──────────────────────────────────────────────────────", file=sys.stderr)
        
        choice = input("Approve architecture phase for this high-criticality task? [y/N]: ").strip().lower()
        
        if choice != "y":
            response = {
                "hookSpecificOutput": {
                    "permissionDecision": "deny",
                    "permissionDecisionReason": "High Criticality Task: Human operator denied the start of the Architecture phase."
                }
            }
            print(json.dumps(response))
            sys.exit(0)

    # If not high criticality, or if human approved, allow execution
    response = {
        "hookSpecificOutput": {
            "permissionDecision": "allow"
        }
    }
    print(json.dumps(response))
    sys.exit(0)

if __name__ == "__main__":
    main()