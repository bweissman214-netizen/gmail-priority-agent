
#!/usr/bin/env python3
  """
  Gmail Priority Tagger Agent
  ============================                                                                                                                                                    
  Scans all unread inbox emails and sorts them into two labels:
    - Priority (Label_26): emails from real people or requiring action
    - Non-Priority (Label_27): everything else — archived out of inbox

  Run by a Claude Code cloud agent using Gmail MCP tools.
  Owner: bweissman214@gmail.com
  """

  # ── Configuration ────────────────────────────────────────────────────────────
                                                                                                                                                                                  
  PRIORITY_LABEL_ID     = "Label_26"   # "Priority"
  NON_PRIORITY_LABEL_ID = "Label_27"   # "Non-Priority"
  SEARCH_QUERY          = "in:inbox is:unread"
  PAGE_SIZE             = 50

  # ── Importance criteria ───────────────────────────────────────────────────────
  #
  # Label PRIORITY if ANY of the following are true:
  #
  #   1. REAL PERSON sender
  #      - Real first/last name in address (e.g. isaac@amtecadvisory.com)
  #      - Exclude: no-reply@, noreply@, newsletter@, notifications@, alerts@,
  #        donotreply@, info@, support@, hello@, team@, news@, marketing@,
  #        updates@, contact@, postmaster@, or obvious bulk-mail domains
  #
  #   2. FINANCIAL ALERT requiring action
  #      - Balance at/below zero, insufficient funds, payment overdue, fraud alert
  #
  #   3. MEETING INVITATION from a real individual (not a mailing list)
  #
  #   4. JOB APPLICATION RESPONSE from a named recruiter or HR person
  #
  #   5. ACCOUNT ACTION REQUIRED
  #      - A real company asking you to confirm/verify something important
  #        (e.g. AmEx income confirmation, bank security alert)
  #
  # Label NON-PRIORITY (everything else) and ARCHIVE (remove INBOX label):
  #   - Newsletters, digests, Substack, Morning Brew, etc.
  #   - Marketing / promotional emails
  #   - Automated receipts, shipping updates, confirmations
  #   - Social media digests
  #   - Job board automated alerts
  #   - App updates / product announcements
  #   - Religious content / Torah learning notifications
  #   - Event invitations from organizations / mailing lists

  # ── Agent instructions ────────────────────────────────────────────────────────
  #
  #   Step 1 — Search inbox                                                                                                                                                       
  #       Call search_threads(query="in:inbox is:unread", pageSize=50)
  #       Paginate through ALL pages using nextPageToken until done.
  #
  #   Step 2 — Classify each thread
  #       Evaluate sender and subject against the criteria above.                                                                                                                 
  #       Every thread gets exactly ONE label.
  #
  #   Step 3 — Apply labels
  #       PRIORITY:     label_thread(threadId, labelIds=["Label_26"])
  #       NON-PRIORITY: label_thread(threadId, labelIds=["Label_27"])
  #                     unlabel_thread(threadId, labelIds=["INBOX"])  ← archives it
  #
  #   Step 4 — Print summary
  #       - Total threads scanned
  #       - Priority count + list (sender | subject)                                                                                                                              
  #       - Non-Priority count (archived out of inbox)

  def run():
      """Entry point — executed by the Claude Code agent using Gmail MCP tools."""
      pass

  if __name__ == "__main__":
      run()                        
