# gmail-priority-agent

  This agent auto-organizes your Gmail inbox by flagging important emails.
  It scans your inbox daily and applies a **Priority** label to emails that matter.

  ## What it does
  - Runs every morning Sunday–Friday at 8am ET (skips Saturday for Shabbat)
  - Scans the past 24 hours of inbox
  - Applies the **Priority** label to emails from real people or requiring action
  - Ignores newsletters, marketing, and automated notifications

  ## What counts as "Priority"
  - Email from a real individual person
  - Financial alerts (low balance, overdraft, payment due)
  - Meeting invitations from real people
  - Job application responses
  - Account actions requiring a response

  ## Files
  - `gmail_tagger.py` — classification logic and agent instructions
  
  ## How to update the rules
  Edit `gmail_tagger.py` and push to `main`. The agent picks up changes automatically on the next morning's run.

  ## Infrastructure
  - Runs as a Claude Code cloud routine (Sunday–Friday, 8am ET)
  - Uses Gmail MCP connector (Label ID: `Label_26`, display name: `Priority`)
  - Manage the routine: https://claude.ai/code/routines/trig_01HwCJQfioewudGzStW4BYu4
