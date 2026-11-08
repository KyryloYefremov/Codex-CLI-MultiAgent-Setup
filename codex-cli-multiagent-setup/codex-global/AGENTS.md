# Personal Defaults

## Code Style & Formatting
- Prefer explicit types over implicit inferences.
- Use early returns and guard clauses to reduce nesting depth.
- Write concise, readable code comments focused on "why" rather than "what".

## Security & Environment Safety
- NEVER output secrets, API keys, `.env` file contents, or private credentials in agent outputs.
- Never run destructive shell commands (e.g., `rm -rf /`, `git push --force`) without explicit human confirmation.
- Output clean Markdown without unnecessary fluff or excessive meta-announcements.