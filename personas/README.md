personas/

This folder contains short persona cards and prompt templates to use during "vibe coding".

Files
- 01-requirements-architect.md
- 02-rapid-implementer.md
- 03-perfection-engineer.md
- 04-pairing-qa.md
- 05-zen-integrator.md

How to use
1. Open the persona file and fill placeholders in the Prompt Template.
2. Copy the filled prompt into your chat or assistant session.
3. Use editor snippets or a small script to paste templates quickly (PowerShell: Get-Content | Set-Clipboard).

Commit workflow
- Edit persona files as your practices evolve. Keep them short and versioned with the repo.

Switching tips
- Map persona files to editor snippets (e.g., VS Code).
- Quick CLI: `Get-Content .\personas\01-requirements-architect.md | Set-Clipboard` (PowerShell) to copy to clipboard.
