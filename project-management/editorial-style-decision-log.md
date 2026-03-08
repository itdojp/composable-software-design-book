# Editorial Style Decision Log

## Purpose

This log records recurring editorial choices that should stay stable across later copyedits.
Use it when a local rewrite looks reasonable but risks drifting from the house style or glossary.

## Stable decisions

| Topic | Decision | Reason |
| --- | --- | --- |
| AI terminology | Prefer `AI-assisted` for workflows and `AI agent` for the acting software component. | This keeps the prose practical without overusing `agentic` as a catch-all adjective. |
| View terminology | Keep `runtime view` and `reviewer view` as canonical open compounds. | They align with Appendix B and the chapter-level terminology bridge in Appendix C. |
| Boundary terminology | Keep `responsibility boundary`, `shared boundary`, `synchronization boundary`, and `effect boundary` as reader-facing control terms. | They tie the formal vocabulary to architecture and workflow consequences. |
| Artifact capitalization | Capitalize canonical artifact names when they refer to the running example's durable artifact classes. | This preserves cross-file traceability and reduces glossary drift. |
| Claim IDs | Keep claim IDs in figure captions, review callouts, and traceability artifacts, not in ordinary explanatory prose. | This preserves reader flow while keeping review anchors visible where they matter. |
| Chapter openings | Open with the immediate design tension before naming the chapter's formal move. | This reduces template feel and strengthens chapter-to-chapter narrative flow. |
| Chapter endings | End with the next design pressure rather than a generic restatement of the current chapter. | This keeps the manuscript reading like one book instead of disconnected packets. |
| Figure takeaway line | Use one explicit `Reader takeaway` sentence between caption and figure body. | This makes the figure claim readable in print, web, and ebook contexts. |

## Update rule

- Add a new entry only when the same style question has appeared in multiple files.
- When a decision changes, update `docs/style/house-style.md`, affected chapters, and glossary wording in the same change set.
