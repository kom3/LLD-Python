In **LLD (Low-Level Design) interviews**, interviewers mainly evaluate how you **think**, **structure a solution**, and **translate requirements into clean, extensible code/design**. Here’s a **clear step-by-step approach** you should follow during the interview.

---

## You can approach the design with either Top-Down approach or the Bottom-Up approach

## 1. Clarify Requirements (Very Important)

Before designing anything:

* Ask **functional requirements**

  * What exactly should the system do?
  * Inputs / outputs?
  * Constraints or edge cases?
* Ask **non-functional requirements**

  * Performance?
  * Scalability?
  * Thread-safety?
  * Extensibility?

👉 *Never assume.* Clarifying shows maturity.

---

## 2. Identify Core Use Cases

* List the **main operations** the system must support
  (e.g., *book ticket, cancel ticket, search flights*).
* Prioritize **happy path first**, then edge cases.

This helps scope your design.

---

## 3. Identify Key Entities (Classes)

* Extract **nouns** from requirements → potential classes.
* Define:

  * Core domain classes
  * Supporting/helper classes
* Avoid premature abstraction.

Example:

```
User, Order, Product, Payment, Inventory
```

---

## 4. Define Responsibilities (SRP)

For each class:

* What is it responsible for?
* What should it **NOT** do?

Follow **Single Responsibility Principle**:

* One reason to change per class.

---

## 5. Define Relationships

Decide:

* **Association**
* **Aggregation**
* **Composition**
* **Inheritance vs Composition**

Explain *why* you chose one.

---

## 6. Create UML diagrams (lightweight)
    Rule of thumb:
    - If your UML helps the interviewer understand your design faster → it’s correct.
    - Good UML:
    - 5–10 classes max
    - Clear relationships
    - Evolves during discussion

    Bad UML:
    - 20+ classes upfront
    - Over-engineered
    - Drawn before requirements are clear

    How Interviewers Expect You to Use UML

    Typical flow in interview:
    - You talk through requirements

    - You say:
    “Let me draw a quick class diagram to structure this”

    - You draw a simple UML

    - You convert that UML into code

    - This shows structured thinking.


## 7. Design Interfaces & APIs

* Define **public methods** for each class.
* Prefer **interfaces** for behaviors that may change.
* Think in terms of **contracts**.

Example:

```
PaymentService
 ├── pay()
 ├── refund()
```

---

## 8. Apply Design Patterns (Only If Needed)

Use patterns **only when justified**:

* Factory → object creation
* Strategy → interchangeable behaviors
* Observer → event-based updates
* Singleton → shared resources (be careful)

⚠️ Don’t force patterns.

---

## 9. Handle Edge Cases & Constraints

Discuss:

* Invalid inputs
* Failures
* Concurrency (if applicable)
* Exception handling

This separates good from great candidates.

---

## 10. Write Clean, Modular Code (or Pseudocode)

* Start with **class skeletons**
* Add methods gradually
* Keep code readable
* Use meaningful names

Interviewers prefer **correct + readable** over clever.

---

## 11. Discuss Extensibility & Trade-offs

Answer questions like:

* How would you add a new feature?
* What happens if requirements change?
* What trade-offs did you make?

This shows real-world thinking.

---

## 12. Quick Review & Improvements

Before ending:

* Summarize your design
* Mention possible improvements if given more time

---

## Interviewer’s Evaluation Checklist

They look for:

* Clear thought process
* SOLID principles
* Object-oriented thinking
* Communication skills
* Maintainability over perfection

---

### One-Line Interview Mantra

> **“Clarify → Model → Design → Code → Justify”**

