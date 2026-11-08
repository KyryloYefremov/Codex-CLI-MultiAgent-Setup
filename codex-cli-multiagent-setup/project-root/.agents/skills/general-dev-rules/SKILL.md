---
name: general-dev-rules
description: Baseline repository code style, engineering patterns, and documentation standards.
---

# General Development Standards

Whenever you write or modify code in this repository, you must strictly adhere to the following standards:

## 1. Code Style & Architecture
- **DRY & SOLID:** Do not repeat yourself. Extract shared logic into utility functions. Adhere to Single Responsibility Principles.
- **Early Returns:** Avoid deep nesting (e.g., multiple `if/else` blocks). Use guard clauses and early returns at the top of functions.
- **Strict Typing:** Never use implicit `any` in when a typed data class/interface can be used.
- **KISS:** Keep it simple and stupid, do not over-engineer solutions. Avoid unnecessary abstractions or patterns that do not add value.

## 2. Documentation & Docstrings
- **File Headers:** Do not add file-level author headers.
- **Docstrings:** All available functions, classes, and complex logic blocks MUST include comprehensive docstrings describing inputs, outputs, and side effects.
- **Inline Comments:** Focus inline comments entirely on the *WHY*, not the *WHAT*. Assume the reader understands the syntax but needs to know the business reason behind the logic.

## 3. Error Handling
- Never swallow exceptions silently (e.g., empty `catch` or `except` blocks). Always log the error trace and bubble up handled custom error classes to the caller.