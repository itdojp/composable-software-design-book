---
layout: book
title: "Preface"
description: "Origin, scope, and promise of the book for engineers designing AI-assisted systems."
---

# Preface

This book began with a practical engineering problem.
Teams were adding AI assistance to software delivery faster than they were improving the artifact boundaries that explain who proposed a change, who approved it, and which evidence justified execution.
That mismatch is now a design and governance problem for mainstream software teams, not a niche tooling concern.

That gap is not solved by telling engineers to be careful.
It is solved by giving them a design language that connects architecture decisions, review checkpoints, operational traces, and verification consequences.
This manuscript uses category-theoretic vocabulary for that purpose, but it does so selectively.
The goal is not to turn working engineers into pure mathematicians.
The goal is to make compositional reasoning usable at the point where AI-assisted work becomes a governance, safety, or audit concern.
It is therefore not a general AI-assisted engineering handbook and not a broad category theory survey.
It is a book about governed AI-assisted delivery for readers who need formal discipline and operational realism at the same time.

The running example stays small on purpose.
It lets the reader see one governed approval path repeatedly while the formal vocabulary grows around it.
That design choice reflects the book's core promise.
If a concept cannot improve one bounded engineering workflow, it does not belong here as a central technique.

This book should therefore be read as the primary explanation of the method.
Readers who want file-level examples, validators, and versioned artifacts can use the companion repository after the chapter argument is clear.
The explanation belongs in the book.
The companion material exists to deepen inspection, not to carry the method in place of the prose.
