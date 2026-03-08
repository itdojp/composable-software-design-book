---
layout: book
title: "Monads, Kleisli Composition, and Effect Boundaries"
chapter: chapter09
order: 10
description: "Make effects explicit so agent orchestration remains safe, reviewable, and testable."
---

# Monads, Kleisli Composition, and Effect Boundaries

This chapter makes effects explicit so AI-assisted orchestration remains safe, reviewable, and testable.

## Why effects need explicit boundaries

This section frames side effects as design commitments that must be visible to reviewers and operators.

### Side effects as design commitments

### The cost of hidden operational behavior

## Monads as operational envelopes

This section explains how monadic structure separates pure reasoning from effectful execution.

### Pure core and effectful shell

### Reading unit and bind in engineering terms

## Kleisli composition for agent orchestration

This section uses Kleisli composition to model chained tool calls, prompts, and execution contexts.

### Tool calls, prompts, and execution context

### Chaining effectful steps safely

## Managing error, state, I/O, and external tools

This section compares common effect classes and the tradeoffs of making one dominant in a workflow.

### Choosing the dominant effect model

### Composing multiple effects without confusion

## Effect containment in production systems

This section closes with operational guidance for rollback, audit, and controlled escape hatches.

### Reviewable escape hatches

### Operational limits, rollback, and audit
