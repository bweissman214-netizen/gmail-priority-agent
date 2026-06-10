#!/usr/bin/env python3
  """
  Gmail Priority Tagger Agent
  ============================
  Scans the Gmail inbox for the past 24 hours and applies the "Priority"
  label (Label_26) to emails that are important.
  
  Run by a Claude Code cloud agent using Gmail MCP tools.
  Owner: bweissman214@gmail.com
  """

  # ── Configuration ────────────────────────────────────────────────────────────
  
  LABEL_ID    = "Label_26"   # Gmail label ID for "Priority"
  LABEL_NAME  = "Priority"
  SEARCH_QUERY = "in:inbox newer_than:1d"
  PAGE_SIZE   = 50

  # ── Importance criteria ───────────────────────────────────────────────────────
  #
  # Label a thread IMPORTANT if ANY of the following are true:
  #
  #   1. REAL PERSON sender
  #      - Email address contains a real first/last name (e.g. john.smith@company.com,
  #        isaac@amtecadvisory.com, suzanne.george@73strings.com)
  #      - Exclude: no-reply@, noreply@, newsletter@, notifications@, alerts@,
  #        donotreply@, info@, support@, hello@, team@, news@, marketing@,
  #        updates@, contact@, postmaster@, and obvious bulk-mail domains
  #
  #   2. FINANCIAL ALERT requiring action
  #      - Bank balance at/below zero or insufficient funds (Wells Fargo, Chase, etc.)
  #      - Payment overdue / fraud alert / card action required
  #
  #   3. MEETING INVITATION from a real individual
  #      - Calendar invite sent by a named person (not a mailing list)
  #
  #   4. JOB APPLICATION RESPONSE
  #      - From a named recruiter or HR person, not an automated ATS system
  #
  #   5. ACCOUNT ACTION REQUIRED
  #      - A real company asking you to confirm/verify something important
  #        (e.g. AmEx income confirmation, bank security alert)
  #
  # Do NOT label:
  #   - Newsletters (Morning Brew, The Atlantic, Substack, etc.)
  #   - Marketing / promotional emails
  #   - Automated receipts, shipping updates, membership confirmations
  #   - Social media digests (Instagram, LinkedIn)
  #   - Job board automated alerts
  #   - App update / product announcement emails
  #   - Religious content / Torah learning notifications
  #   - Event invitations from organizations / mailing lists
  
  # ── Agent instructions ────────────────────────────────────────────────────────
  #
  # The Claude Code agent executing this file should:
  #
  #   Step 1 — Search inbox
  #       Call search_threads(query=SEARCH_QUERY, pageSize=PAGE_SIZE)
  #       If nextPageToken is present, paginate until all threads are fetched.
  #
  #   Step 2 — Classify each thread
  #       For each thread, evaluate sender address and subject line against
  #       the criteria above. When in doubt, do NOT label.
  #
  #   Step 3 — Apply label
  #       For each IMPORTANT thread, call:
  #           label_thread(threadId=<id>, labelIds=[LABEL_ID])
  #
  #   Step 4 — Print summary
  #       Output:
  #           - Total threads scanned
  #           - Number labeled Priority
  #           - List of labeled threads: sender | subject

  def run():
      """Entry point — executed by the Claude Code agent using Gmail MCP tools."""
      pass
  
  if __name__ == "__main__":
      run()

  5. Click Commit changes

