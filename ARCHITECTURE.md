# Architecture Overview

This document defines the **conceptual architecture** of the Momentum project. It is intentionally brief and serves as a shared mental model for both human developers and AI-assisted tools.

The goal is clarity of responsibility, strict boundaries, and low coupling between components.

---

## High-Level Flow

User action → User State → Rule Engine → Strategy Selector → Agent → Task → User

At no point does the AI agent modify curriculum, rules, or system state directly.

---

## Core Components

### 1. Curriculum

**Responsibility:**

* Defines the fixed learning path
* Contains ordered learning steps (e.g., Android / Jetpack Compose concepts)

**Notes:**

* Fully deterministic
* Never modified by the agent
* Provides context only

---

### 2. User State

**Responsibility:**

* Tracks current curriculum step
* Records inactivity, postponement, and recent actions

**Notes:**

* Simple, explicit signals only
* No inferred or external data sources

---

### 3. Rule Engine

**Responsibility:**

* Evaluates user state
* Detects when intervention is required

**Output:**

* A high-level intervention signal (e.g., inactivity detected)

**Notes:**

* Fully deterministic
* No AI involvement

---

### 4. Strategy Selector

**Responsibility:**

* Maps rule outcomes to an intervention strategy

**Examples:**

* Normal progress
* Change task type
* Aggressive scope reduction

**Notes:**

* Strategy selection is rule-based
* Strategies constrain, but do not define, tasks

---

### 5. Task Template Library

**Responsibility:**

* Defines a bounded set of allowed task patterns per curriculum step

**Examples:**

* Inspect
* Rename
* Modify (Small)
* Add (Minimal)
* Refactor (Micro)

**Notes:**

* Tasks are templates, not instructions
* This library defines the agent’s action space

---

### 6. Agent Interface

**Responsibility:**

* Receives constrained input from the system
* Selects and instantiates exactly one task
* Phrases the task in human-friendly language

**Input:**

* Current step context
* Selected strategy
* Allowed task templates
* Recent task history

**Output:**

* A single task description (text only)

**Notes:**

* The agent does not manage flow or state
* The agent does not plan or sequence actions

---

### 7. Persistence Layer

**Responsibility:**

* Stores user state and interaction history

**Notes:**

* Implementation-agnostic
* No business logic

---

### 8. UI Layer

**Responsibility:**

* Displays current task and context
* Collects explicit user input (completed / postponed)

**Notes:**

* Minimal UI
* No logic beyond event forwarding

---

## Design Constraints (Non-Negotiable)

* The AI agent operates only within a bounded action space
* Only one task is presented at any time
* Curriculum and rules are deterministic
* Failure reduces scope; it never escalates difficulty

---

## Guiding Principle

> Architecture exists to make incorrect behavior impossible.