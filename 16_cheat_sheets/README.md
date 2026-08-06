# 📄 Print-Ready Cheat Sheets — 1 página por concepto

> **Para imprimir y revisar** justo antes del examen. Cada sheet es 1 página.

---

## 🗂️ Índice

| Sheet | Página | Cuándo usarla |
|---|---|---|
| CS-01: Los 7 Principios | Sheet 1 | Memoria pura |
| CS-02: Tipos de Testing | Sheet 2 | Diferenciar conceptos |
| CS-03: Test Pyramid + Quadrants | Sheet 3 | Cap 5 (NEW v4.0) |
| CS-04: Decision Tables | Sheet 4 | Cap 4 — técnica más preguntada |
| CS-05: BVA 2-value vs 3-value | Sheet 5 | Cap 4 — boundary |
| CS-06: Equivalence Partitioning | Sheet 6 | Cap 4 — particiones |
| CS-07: Coverage Metrics | Sheet 7 | Cap 4 — métricas |
| CS-08: State Transition Diagrams | Sheet 8 | Cap 4 — estados |
| CS-09: Review Types | Sheet 9 | Cap 3 — formalidad |
| CS-10: Risk Calculation | Sheet 10 | Cap 5 — risk = likelihood × impact |
| CS-11: ISTQB Question Patterns | Sheet 11 | Cualquier cap — patterns |
| CS-12: Cap 4 Cheat Sheet | Sheet 12 | Resumen visual Cap 4 |
| CS-13: ISO 25010 (2023) | Sheet 13 | Cap 1 — quality model |
| CS-14: Defect Categories | Sheet 14 | Cap 1 — failure/deffect |
| CS-15: Final Day Checklist | Sheet 15 | Día del examen |

---

## Sheet 1 — CS-01: Los 7 Principios

```
┌────────────────────────────────────────────────────────────────┐
│  LOS 7 PRINCIPIOS DE TESTING (ISTQB CTFL v4.0.1)              │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  1. TESTING SHOWS THE PRESENCE OF DEFECTS                      │
│     ✓ No su absence — tests find bugs, but can't prove no bugs│
│                                                                │
│  2. EXHAUSTIVE TESTING IS IMPOSSIBLE                          │
│     ✓ Need risk-based prioritization + sampling               │
│                                                                │
│  3. EARLY TESTING SAVES TIME AND MONEY                        │
│     ✓ Shift-left — test from requirements phase               │
│                                                                │
│  4. DEFECTS CLUSTER TOGETHER                                  │
│     ✓ 80/20 rule — small modules often have most bugs         │
│                                                                │
│  5. BEWARE OF THE PESTICIDE PARADOX                           │
│     ✓ Same tests over time find fewer new bugs — refresh       │
│                                                                │
│  6. TESTING IS CONTEXT-DEPENDENT                              │
│     ✓ Safety-critical ≠ e-commerce ≠ mobile game              │
│                                                                │
│  7. ABSENCE-OF-ERRORS IS A FALLACY                            │
│     ✓ 99% bug-free but unusable = failure                     │
│                                                                │
│  ─────────────────────────────────────────────────────────    │
│  MEMORIZE: "Presence / Exhaustive / Early / Cluster /         │
│           Pesticide / Context / Absence"                      │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 2 — CS-02: Tipos de Testing

```
┌────────────────────────────────────────────────────────────────┐
│  TIPOS DE TESTING — CHEAT SHEET                              │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  TEST LEVELS (Cap 2.2):                                       │
│  ┌──────────────┬──────────────────────────────────┐          │
│  │ Level        │ Tests what                       │          │
│  ├──────────────┼──────────────────────────────────┤          │
│  │ Component    │ Individual components            │          │
│  │ Integration  │ Components together              │          │
│  │ System       │ Complete system                  │          │
│  │ Acceptance   │ Business / user acceptance       │          │
│  └──────────────┴──────────────────────────────────┘          │
│                                                                │
│  TEST TYPES (cross-cutting):                                  │
│  • Functional: What system does                               │
│  • Non-functional: How well (perf, security, usability)       │
│  • Change-related: Confirmation + Regression                  │
│  • Maintenance: After release                                │
│                                                                │
│  TESTING APPROACHES:                                          │
│  • Manual vs Automated                                        │
│  • Static vs Dynamic                                          │
│  • Specification vs Structure vs Experience-based             │
│                                                                │
│  KEY DISTINCTIONS:                                            │
│  • Confirmation = re-test that specific bug                   │
│  • Regression = tests nothing else broke                      │
│  • Functional vs Non-functional: what vs how                  │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 3 — CS-03: Test Pyramid + Quadrants

```
┌────────────────────────────────────────────────────────────────┐
│  TEST PYRAMID (Cap 5.1.6) ⭐ NEW v4.0                        │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│                          /\                                   │
│                         /  \                                  │
│                        / E2E\         ~10%                   │
│                       / UI  \          (slow, expensive)      │
│                      /──────\                                │
│                     / Integ. \        ~20%                   │
│                    / API      \                               │
│                   /────────────\                              │
│                  /    Unit      \    ~70%                    │
│                 /  Components    \     (fast, cheap)          │
│                /──────────────────\                          │
│                                                                │
│  ⚠️ INVERTED PYRAMID = FLAKY, SLOW CI = BAD                  │
│                                                                │
│  TESTING QUADRANTS (Cap 5.1.7) ⭐ NEW v4.0                   │
│  ─────────────────────────────────────────────────────────    │
│  ┌─────────────────┬─────────────────┐                       │
│  │ Q1              │ Q2              │                       │
│  │ Tech-facing     │ Business-facing │                       │
│  │ Support team    │ Support team    │                       │
│  │ Component +     │ Functional +    │                       │
│  │ Integration     │ System + Story  │                       │
│  ├─────────────────┼─────────────────┤                       │
│  │ Q3              │ Q4              │                       │
│  │ Business-facing │ Tech-facing     │                       │
│  │ Critique        │ Critique        │                       │
│  │ Exploratory +   │ Performance +   │                       │
│  │ Usability + UAT │ Security +      │                       │
│  │                 │ Scalability     │                       │
│  └─────────────────┴─────────────────┘                       │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 4 — CS-04: Decision Tables

```
┌────────────────────────────────────────────────────────────────┐
│  DECISION TABLES (Cap 4.2.3)                                  │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  EXAMPLE: "Premium discount"                                 │
│  Conditions:                                                  │
│    C1: Customer is member (Y/N)                              │
│    C2: Cart > $100 (Y/N)                                     │
│    C3: Promo code applied (Y/N)                              │
│  Actions:                                                     │
│    A1: 5% discount                                            │
│    A2: Free shipping                                          │
│                                                                │
│  ┌────┬────┬────┬────┬────┐                                  │
│  │ C1 │ C2 │ C3 │ A1 │ A2 │                                  │
│  ├────┼────┼────┼────┼────┤                                  │
│  │ Y  │ Y  │ Y  │ X  │ X  │  (5% + free ship)               │
│  │ Y  │ Y  │ N  │ X  │ X  │                                  │
│  │ Y  │ N  │ Y  │ X  │ -  │                                  │
│  │ Y  │ N  │ N  │ X  │ -  │                                  │
│  │ N  │ Y  │ Y  │ -  │ X  │                                  │
│  │ N  │ Y  │ N  │ -  │ X  │                                  │
│  │ N  │ N  │ Y  │ -  │ -  │                                  │
│  │ N  │ N  │ N  │ -  │ -  │                                  │
│  └────┴────┴────┴────┴────┘                                  │
│                                                                │
│  STEPS:                                                       │
│  1. Identify conditions (inputs)                              │
│  2. Identify actions (outputs)                                │
│  3. List all combinations (2^n)                               │
│  4. Mark which actions fire for each combo                    │
│  5. COLLAPSE redundant columns (same action pattern)          │
│                                                                │
│  ⚠️ ISTQB expects: collapsed tables, not all 2^n             │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 5 — CS-05: BVA 2-value vs 3-value

```
┌────────────────────────────────────────────────────────────────┐
│  BOUNDARY VALUE ANALYSIS (Cap 4.2.2)                         │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  RANGE: 18 to 65 (valid)                                      │
│                                                                │
│  2-VALUE BVA (4 tests):                                       │
│  ┌────────────────────────────────────────────────┐           │
│  │ 17 (just below) │ 18 (boundary) │ 65 (boundary)│ 66 (just above) │
│  └────────────────────────────────────────────────┘           │
│                                                                │
│  3-VALUE BVA (6 tests):                                       │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ 17 │ 18 │ 19 │ 64 │ 65 │ 66                              │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                │
│  WHEN USE 2 vs 3?                                             │
│  • 2-value: simple ranges, less time                          │
│  • 3-value: complex systems, more thorough                    │
│                                                                │
│  RULE OF THUMB:                                               │
│  • 2-value: b-1, b, a, a+1                                   │
│  • 3-value: b-1, b, b+1, a-1, a, a+1                         │
│  (where b=min, a=max)                                         │
│                                                                │
│  ⚠️ v4.0 distinguishes clearly. Old material says "boundaries"│
│     generically — be specific about 2 or 3.                   │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 6 — CS-06: Equivalence Partitioning

```
┌────────────────────────────────────────────────────────────────┐
│  EQUIVALENCE PARTITIONING (Cap 4.2.1)                        │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  EXAMPLE: Age field 18-65                                     │
│                                                                │
│  ┌─────────────────┬──────────────┐                          │
│  │ Partition       │ Examples     │                          │
│  ├─────────────────┼──────────────┤                          │
│  │ INVALID (<18)   │ -5, 0, 17    │ (test with 17)           │
│  │ VALID (18-65)   │ 30, 50       │ (test with 30)           │
│  │ INVALID (>65)   │ 66, 100      │ (test with 70)           │
│  └─────────────────┴──────────────┘                          │
│                                                                │
│  KEY POINTS:                                                   │
│  • 1 test per partition (not per value)                       │
│  • Reduces test count dramatically                             │
│  • Test INVALID partitions separately to avoid masking         │
│  • v4.0 EXPLICITLY says: test invalid in isolation            │
│                                                                │
│  COMMON MISTAKES:                                              │
│  • Missing edge cases (negative numbers, zero, max+1)        │
│  • Grouping valid + invalid in same test (defect masking)     │
│  • Forgetting boundary between partitions                     │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 7 — CS-07: Coverage Metrics

```
┌────────────────────────────────────────────────────────────────┐
│  COVERAGE METRICS (Cap 4.3)                                   │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  STATEMENT COVERAGE:                                          │
│  • % of executable statements run by tests                    │
│  • Code: if (x > 0) y = 1; else y = 2;                       │
│  • Test: x=1 → statement y=1 runs (1/1 = 100%)               │
│                                                                │
│  BRANCH COVERAGE:                                             │
│  • % of decision outcomes (true + false) tested              │
│  • Same code:                                                │
│  • Test 1: x=1 (true branch)                                 │
│  • Test 2: x=-1 (false branch)                               │
│  • 100% branch coverage                                      │
│                                                                │
│  RULE: Branch ≥ Statement (100% branch = 100% statement)    │
│                                                                │
│  COMMON FORMULAS:                                             │
│  • Statement: (statements run) / (total statements)          │
│  • Branch: (branches taken) / (total branches)               │
│                                                                │
│  OTHER COVERAGE TYPES:                                        │
│  • Decision / Branch / Condition / Modified Condition /       │
│    Multiple Condition / Path                                 │
│  • Product coverage (features tested)                        │
│  • Risk coverage (risk addressed)                            │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 8 — CS-08: State Transition Diagrams

```
┌────────────────────────────────────────────────────────────────┐
│  STATE TRANSITION DIAGRAMS (Cap 4.2.4)                       │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  EXAMPLE: ATM Card Lifecycle                                  │
│                                                                │
│           ┌──────┐                                             │
│           │ Idle │                                             │
│           └───┬──┘                                             │
│        insert │                                                │
│               ▼                                                │
│     ┌──────────────────┐                                      │
│     │ Card Inserted    │                                      │
│     └────────┬─────────┘                                      │
│    enter PIN │                                                │
│              ▼                                                │
│     ┌──────────────────┐                                      │
│     │ PIN Entered      │                                      │
│     └────────┬─────────┘                                      │
│     OK PIN  │                                                 │
│              ▼                                                │
│     ┌──────────────────┐                                      │
│     │ Authenticated    │                                      │
│     └────────┬─────────┘                                      │
│   transaction│                                                 │
│              ▼                                                │
│     ┌──────────────────┐                                      │
│     │ Transaction      │                                      │
│     └────────┬─────────┘                                      │
│     eject  │                                                  │
│             ▼                                                 │
│         ┌──────┐                                              │
│         │ Idle │                                              │
│         └──────┘                                              │
│                                                                │
│  TEST DESIGN:                                                 │
│  • 0-switch coverage = each transition tested                 │
│  • 1-switch coverage = pairs of transitions                  │
│  • Also test INVALID transitions (wrong PIN → ?)             │
│                                                                │
│  ⚠️ v4.0 changed name from "state transition diagram" to     │
│     "state diagram" — same concept                           │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 9 — CS-09: Review Types

```
┌────────────────────────────────────────────────────────────────┐
│  REVIEW TYPES (Cap 3.2)                                       │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  FORMALITY (least → most):                                    │
│                                                                │
│  1. INFORMAL REVIEW                                           │
│     • No process, peer asks for feedback                     │
│     • Author-led                                              │
│                                                                │
│  2. WALKTHROUGH                                               │
│     • Author leads, explains                                 │
│     • Educational purpose                                     │
│     • Open discussion                                         │
│                                                                │
│  3. TECHNICAL REVIEW                                          │
│     • Peer review by tech team                               │
│     • Documented                                             │
│     • Finds defects + alternatives                           │
│                                                                │
│  4. INSPECTION (MOST FORMAL)                                  │
│     • Defined process + roles (moderator, reader, scribe)    │
│     • Metrics collected                                       │
│     • Entry/exit criteria                                     │
│     • NOT author-led                                          │
│     • Most rigorous                                           │
│                                                                │
│  KEY DISTINCTIONS:                                            │
│  • Inspection = formal, roles, metrics                       │
│  • Walkthrough = informal, author-led                         │
│  • Technical review = peer-driven                            │
│                                                                │
│  ISTQB expects:                                                │
│  • Roles (moderator, author, reader, scribe, reviewer)        │
│  • Entry criteria (ready for review)                         │
│  • Exit criteria (defects logged)                            │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 10 — CS-10: Risk Calculation

```
┌────────────────────────────────────────────────────────────────┐
│  RISK MANAGEMENT (Cap 5.2)                                    │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  RISK = LIKELIHOOD × IMPACT                                   │
│                                                                │
│  EXAMPLE SCALE:                                               │
│  ┌──────────┬──────────┬──────────┬──────────┐               │
│  │ Likeli.  │ 1 (Low)  │ 2 (Med)  │ 3 (High) │               │
│  ├──────────┼──────────┼──────────┼──────────┤               │
│  │ Impact 1 │ 1        │ 2        │ 3        │               │
│  │ Impact 2 │ 2        │ 4        │ 6        │               │
│  │ Impact 3 │ 3        │ 6        │ 9        │               │
│  └──────────┴──────────┴──────────┴──────────┘               │
│                                                                │
│  RESPONSE STRATEGIES (AMTA + Share):                         │
│  ┌──────────┬──────────────────────────────────┐             │
│  │ Accept   │ Acknowledge, no action          │             │
│  │ Mitigate │ Reduce likeli. or impact        │             │
│  │ Transfer │ Insurance, outsourcing          │             │
│  │ Avoid    │ Don't do the feature            │             │
│  │ Share    │ Multiple parties share risk     │             │
│  └──────────┴──────────────────────────────────┘             │
│                                                                │
│  RISK TYPES:                                                   │
│  • Project risk = schedule/cost/quality of PROJECT           │
│  • Product risk = quality of PRODUCT (security, perf, etc.)  │
│                                                                │
│  PRODUCT RISK CATEGORIES:                                      │
│  • Functional (incorrect output)                              │
│  • Performance (slow)                                         │
│  • Security (vulnerable)                                      │
│  • Compatibility (broken on some browsers)                   │
│  • Usability (poor UX)                                        │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 11 — CS-11: ISTQB Question Patterns

```
┌────────────────────────────────────────────────────────────────┐
│  ISTQB QUESTION PATTERNS — HOW TO READ                       │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  KEYWORD → STRATEGY                                           │
│                                                                │
│  "EXCEPT" → Find the option that does NOT apply              │
│             (rare exception: "all EXCEPT one")               │
│                                                                │
│  "NOT"    → Find the FALSE option                            │
│             Common trick: read carefully                      │
│                                                                │
│  "BEST"   → Choose the MOST correct option                   │
│             Often 2+ look right; pick most specific           │
│                                                                │
│  "MOST"   → Same as BEST                                     │
│             Test what ISTQB thinks is most important         │
│                                                                │
│  "WHICH"  → Sometimes all seem correct; choose               │
│             the one most aligned with ISTQB canon            │
│                                                                │
│  "ALWAYS"/"NEVER" → Almost always FALSE (absolutes)          │
│                                                                │
│  "SHOULD"/"MAY" → Difference between MUST vs CAN             │
│                                                                │
│  "DEPENDING ON CONTEXT" → Testing principle #6 hint         │
│                          Often the right answer              │
│                                                                │
│  "BEFORE" → Process order matters                            │
│             ISTQB has specific order: Plan → Analyze →        │
│             Implement → Execute → Complete                  │
│                                                                │
│  TIPS:                                                         │
│  • Re-read question 2x (especially "EXCEPT", "NOT")          │
│  • Eliminate 2 wrong options first                           │
│  • Look for absolutes (always/never) = red flag = usually F  │
│  • If 2 options seem right, pick more ISTQB-canonical        │
│  • Time yourself: 1.5 min/question                            │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 12 — CS-12: Cap 4 Summary Visual

```
┌────────────────────────────────────────────────────────────────┐
│  CAP 4 TEST ANALYSIS & DESIGN — 1-PAGE OVERVIEW              │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  TECHNIQUES:                                                  │
│                                                                │
│  SPECIFICATION-BASED (BLACK-BOX):                            │
│  ┌─────────────────┬──────────────────────────────────┐       │
│  │ EP              │ Divide inputs into groups        │       │
│  │ BVA             │ Test boundaries (2 or 3-value)   │       │
│  │ Decision Table  │ Combinations of conditions       │       │
│  │ State Diagram   │ States + transitions             │       │
│  │ Use Case        │ Step-by-step scenarios           │       │
│  └─────────────────┴──────────────────────────────────┘       │
│                                                                │
│  STRUCTURE-BASED (WHITE-BOX):                                │
│  ┌─────────────────┬──────────────────────────────────┐       │
│  │ Statement       │ % lines executed                 │       │
│  │ Branch          │ % decision outcomes              │       │
│  └─────────────────┴──────────────────────────────────┘       │
│                                                                │
│  EXPERIENCE-BASED:                                            │
│  ┌─────────────────┬──────────────────────────────────┐       │
│  │ Error Guessing  │ Predict likely bugs              │       │
│  │ Exploratory     │ Learn + design + execute together│       │
│  │ Checklist       │ Guided by pre-made list          │       │
│  └─────────────────┴──────────────────────────────────┘       │
│                                                                │
│  COLLABORATION-BASED (NEW v4.0):                             │
│  ┌─────────────────┬──────────────────────────────────┐       │
│  │ User Story      │ INVEST + 3 amigos                │       │
│  │ ATDD            │ Acceptance tests BEFORE code     │       │
│  └─────────────────┴──────────────────────────────────┘       │
│                                                                │
│  ⚠️ Cap 4 = ~30% of exam. Practice techniques hands-on.      │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 13 — CS-13: ISO 25010 (2023)

```
┌────────────────────────────────────────────────────────────────┐
│  ISO 25010 QUALITY MODEL (UPDATED 2023)                      │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  8 QUALITY CHARACTERISTICS:                                   │
│                                                                │
│  ┌────────────────────┬──────────────────────────────────┐   │
│  │ Functional Suitab. │ Does it do what it should?      │   │
│  │ Performance Eff.   │ Speed, throughput, resources    │   │
│  │ Compatibility      │ Coexists with other systems     │   │
│  │ Interaction Capa.  │ NEW NAME (was Usability)        │   │
│  │ Reliability        │ Works under failure conditions  │   │
│  │ Security           │ Protects data and access        │   │
│  │ Maintainability    │ Easy to modify                  │   │
│  │ Flexibility        │ NEW NAME (was Portability)      │   │
│  └────────────────────┴──────────────────────────────────┘   │
│                                                                │
│  ⚠️ CHANGES v3.1 → v4.0:                                     │
│  • "Usability" → "Interaction Capability"                    │
│  • "Portability" → "Flexibility"                             │
│  • "Safety" ADDED as sub-characteristic                       │
│                                                                │
│  ISTQB CTFL v4.0 includes this update.                       │
│  Material v3.1 may still call them "Usability" — outdated.   │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 14 — CS-14: Defect Categories

```
┌────────────────────────────────────────────────────────────────┐
│  DEFECT / FAILURE / ERROR / MISTAKE                          │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  DEFINITIONS (ISTQB v4.0):                                   │
│                                                                │
│  ERROR (or MISTAKE):                                          │
│  • Human action producing incorrect result                    │
│  • Made by person (typo, misreading, omission)               │
│  • Example: developer typos `==` instead of `>=`            │
│                                                                │
│  DEFECT (or FAULT / BUG):                                    │
│  • Imperfection in code or work product                      │
│  • Result of an error                                         │
│  • Lives in code until fixed                                 │
│                                                                │
│  FAILURE:                                                      │
│  • Observable incorrect behavior                             │
│  • Happens when defect executes                               │
│  • User sees failure                                          │
│                                                                │
│  ROOT CAUSE:                                                   │
│  • Fundamental reason that caused the error                  │
│  • Example: missing requirements review → spec ambiguity    │
│                                                                │
│  CHAIN:                                                        │
│  ┌────────┐ → ┌────────┐ → ┌────────┐                       │
│  │ Error  │   │ Defect │   │ Failure│                       │
│  │ (made) │   │ (in    │   │(when   │                       │
│  │        │   │  code) │   │ runs)  │                       │
│  └────────┘   └────────┘   └────────┘                       │
│                                                                │
│  NOT ALL DEFECTS CAUSE FAILURES:                              │
│  • Code path never executed → defect stays hidden            │
│  • Defect in specific input value only → some users affected│
│                                                                │
│  NOT ALL FAILURES ARE FROM DEFECTS:                          │
│  • Environmental issues (network, hardware)                  │
│  • Incorrect configuration                                    │
│  • User error (wrong input format)                           │
└────────────────────────────────────────────────────────────────┘
```

---

## Sheet 15 — CS-15: Final Day Checklist

```
┌────────────────────────────────────────────────────────────────┐
│  EXAM DAY — FINAL CHECKLIST                                  │
│  ─────────────────────────────────────────────────────────    │
│                                                                │
│  NIGHT BEFORE:                                                │
│  ☐ Sleep 7-8 hours                                           │
│  ☐ Light review only (1 hour max)                            │
│  ☐ Prepare ID + admission ticket + exam voucher              │
│  ☐ Set 2 alarms                                               │
│  ☐ Lay out comfortable clothes                                │
│                                                                │
│  MORNING OF:                                                  │
│  ☐ Eat breakfast (protein + complex carbs)                  │
│  ☐ Hydrate                                                    │
│  ☐ Arrive 30 min early                                       │
│  ☐ No last-minute cramming (stresses brain)                  │
│                                                                │
│  DURING EXAM:                                                 │
│  ☐ Read each question 2x (EXCEPT, NOT, BEST!)               │
│  ☐ First pass: easy questions (30 min)                       │
│  ☐ Skip + bookmark hard ones                                 │
│  ☐ Second pass: hard ones (20 min)                           │
│  ☐ Final review: 10 min                                      │
│  ☐ Don't leave blanks (no penalty for guessing)              │
│                                                                │
│  STRATEGY:                                                    │
│  ☐ 65% = 26/40 needed to pass                                │
│  ☐ Eliminate 2 wrong options first                            │
│  ☐ Look for absolutes (always/never) = usually false         │
│  ☐ Trust your first instinct (usually right)                  │
│  ☐ Time: 1.5 min/question                                    │
│                                                                │
│  REMEMBER:                                                    │
│  ☐ ISTQB is curving toward PRINCIPLES                        │
│  ☐ Context-dependent principle is often the answer           │
│  ☐ "Test pyramid" + "testing quadrants" are NEW v4.0         │
│  ☐ Cap 4 has highest weight (30%)                            │
│  ☐ Process order: Plan → Analyze → Implement → Execute →    │
│    Complete                                                  │
│                                                                │
│  ─────────────────────────────────────────────────────────    │
│  You've prepared. Trust yourself. Good luck! 🍀               │
└────────────────────────────────────────────────────────────────┘
```

---

## 📋 Cómo usar estos cheat sheets

1. **Imprimir todos (PDF reader + print to PDF)** — 1 página por sheet
2. **Revisar 1 por día** durante la semana previa al examen
3. **Llevar al examen si está permitido** (algunos centros lo permiten)
4. **Compartir con el grupo ISTQB PY** — todos los 6 miembros del grupo

---

## 🔗 Links externos útiles

- **istqb.guru CTFL Cheat Sheet:** https://www.istqb.guru/istqb-ctfl-cheat-sheet/
- **OpenExamPrep:** https://open-exam-prep.com/cheat-sheet/istqb-foundation
- **TestPad cheat sheets:** https://www.testpad.com/istqb-cheat-sheets (verify)
