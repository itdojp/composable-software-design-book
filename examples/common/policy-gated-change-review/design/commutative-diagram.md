---
title: "Example Design: Commutative Diagram"
description: "Design diagram for the running example."
---

# Example Design: Commutative Diagram

This diagram states the approval claim that the example carries through the book.

```mermaid
flowchart LR
  CR[Change Request] -->|derive review plan| RP[Review Plan]
  RP -->|human approval| AC[Approved Change]
  CR -->|policy-gated approval path| AC
  CR -->|policy check| PC[Policy Check]
  PC -->|satisfied| RP
```

The direct approval path is only valid when the policy check preserves the meaning of the request and the review plan.
That claim becomes the example's commutative reading in later chapters.
