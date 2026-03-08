---
title: "Minimal Example Diagram"
description: "The smallest diagram used by the running example."
---

# Minimal Example Diagram

The diagram below names the composite approval path that the book reuses in later chapters.

```mermaid
flowchart LR
  CR[Change Request] -->|draft-review-plan| RP[Review Plan]
  RP -->|human-approval| AC[Approved Change]
  CR -->|policy-gated-approval| AC
```

The direct edge `policy-gated-approval` stands for the composition of `draft-review-plan` and `human-approval`.
This gives the reader one stable claim to revisit in later chapters.
