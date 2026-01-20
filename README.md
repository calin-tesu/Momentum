# Momentum

**Momentum** is an agentic learning companion designed to help self-directed developers resume progress when motivation drops or learning is postponed.

The system is intentionally simple and bounded.

---

## Core Idea

Momentum does **not** generate curriculum, plans, or long-term goals.

Instead, it:

* operates on a **fixed learning path** defined by the developer
* uses **deterministic rules** to detect inactivity or repeated postponement
* delegates the choice of the **next small action** to an AI agent

The purpose of the AI is to make *continuation easier than quitting*.

---

## Role of AI (Important)

The AI agent:

* does **not** decide what to learn
* does **not** generate new learning steps
* does **not** optimize for speed or completion

The AI **only**:

* selects one task from a **bounded task template library**
* adapts its scope based on user behavior
* phrases the task in a low-pressure, human-friendly way

All curriculum structure, rules, and constraints are deterministic.

---

## System Overview

1. The user follows a predefined learning path (e.g., Android / Jetpack Compose)
2. The system tracks completion, postponement, and inactivity
3. Rule-based logic selects an intervention strategy
4. The AI agent selects and instantiates **one** minimal next action
5. The user either completes or postpones the action

Only one task is presented at any time.

---

## Design Principles

* Small steps beat perfect plans
* Restarting matters more than speed
* Scope reduction is preferable to pressure
* AI judgment is bounded and explainable

---

## Explicit Non-Goals

Momentum does **not** aim to:

* replace structured courses
* act as a general productivity tool
* monitor external activity (e.g., GitHub)
* provide motivational coaching or reminders

---

## Evaluation

The project is evaluated using **Comet’s Opik**, focusing on:

* appropriateness of selected tasks
* quality of scope adaptation
* alignment between strategy and action

Completion rates are not the primary success metric.

---

This README is intentionally concise to serve as **ground truth** for both developers and AI-assisted tools.
