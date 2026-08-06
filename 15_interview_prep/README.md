# 💼 QA Interview Prep — Preguntas reales + cómo responderlas

> **Después de aprobar el CTFL** — esto es lo que te van a preguntar en interviews de QA.
> 60 preguntas + frameworks de respuesta + ejemplos.

---

## 🎯 Cómo funcionan las interviews de QA

### Tipos de rounds (varía por empresa)

1. **Recruiter screen (15-30 min)** — inglés/español, fit básico
2. **Technical phone screen (45-60 min)** — conceptos ISTQB + basic coding
3. **Live coding (60-90 min)** — escribir SQL/Python/JavaScript en vivo
4. **System design / Test design (60 min)** — diseñar test strategy para una app
5. **Behavioral (45-60 min)** — STAR stories
6. **Manager round (45 min)** — experiencia + motivación

### Para LATAM remote US:
- **Inglés B2+ mínimo** — muchas companies remote-first
- **Screening en inglés** — preparate
- **Tech stack moderno** — Playwright > Selenium para 2025
- **AI knowledge** — diferenciador

---

## 📚 SECCIÓN 1: ISTQB Questions (40 preguntas frecuentes)

### Cap 1 — Fundamentals

**Q1: What are the 7 principles of testing?**
<details>
<summary>✅ Respuesta sugerida</summary>

1. Testing shows the presence of defects, not their absence
2. Exhaustive testing is impossible
3. Early testing saves time and money
4. Defects cluster together
5. Beware of the pesticide paradox
6. Testing is context-dependent
7. Absence-of-errors is a fallacy

Cada uno con un ejemplo de proyecto real.
</details>

**Q2: What's the difference between error, defect, and failure?**
<details>
<summary>✅ Respuesta</summary>

- **Error / Mistake:** Human action that produces incorrect result (typo in code)
- **Defect (Fault / Bug):** Imperfection in the code/work product
- **Failure:** Observable incorrect behavior (when defect executes)
- **Root cause:** Fundamental reason that caused the error

Cadena: Error → Defect → Failure (if executed)
</details>

**Q3: What's the difference between verification and validation?**
<details>
<summary>✅ Respuesta</summary>

- **Verification:** "Are we building the product right?" — confirms work products meet specs
- **Validation:** "Are we building the right product?" — confirms meets user needs

Example: Software passes all unit tests (verification ✓) but UX is awful (validation ✗)
</details>

**Q4: What are the 5 test process activities?**
<details>
<summary>✅ Respuesta</summary>

1. **Test Planning** — define strategy, resources
2. **Test Analysis & Design** — review requirements, identify conditions, design test cases
3. **Test Implementation & Execution** — setup, run tests, log results
4. **Evaluating Exit Criteria & Reporting** — check completion, report
5. **Test Closure Activities** — lessons learned, archive

ISTQB standard process.
</details>

**Q5: What's the difference between root cause and symptom?**
<details>
<summary>✅ Respuesta</summary>

- **Symptom:** What you observe (login fails)
- **Root cause:** Why it happens (auth service timeout)

ISTQB emphasizes finding root causes to prevent recurrence.
</details>

---

### Cap 2 — Testing Throughout SDLC

**Q6: What are the 4 test levels?**
<details>
<summary>✅ Respuesta</summary>

1. **Component testing (unit)** — individual components
2. **Integration testing** — components together
3. **System testing** — complete system
4. **Acceptance testing** — by users/business

Each level has different objectives, test basis, and typical defects found.
</details>

**Q7: What's shift-left testing?**
<details>
<summary>✅ Respuesta</summary>

Testing earlier in SDLC. Moving activities (test design, reviews, static analysis) from end to beginning.

Benefits: cheaper to fix defects found early.

ISTQB v4.0.1 added this concept explicitly.
</details>

**Q8: What's DevOps and how does it impact testing?**
<details>
<summary>✅ Respuesta</summary>

DevOps = culture + practices combining Dev + Ops. Continuous delivery.

Impact on testing:
- Automated testing in CI/CD
- Continuous testing
- Test infrastructure as code
- Faster feedback loops
</details>

**Q9: What's the difference between regression and confirmation testing?**
<details>
<summary>✅ Respuesta</summary>

- **Confirmation (re-test):** Confirms specific defect is fixed
- **Regression:** Ensures changes didn't break existing functionality

Confirmation is narrow; regression is broad.
</details>

**Q10: What's maintenance testing?**
<details>
<summary>✅ Respuesta</summary>

Testing after release for:
- Bug fixes
- Enhancements
- Migration to new platforms
- Retirement

Often reuses existing testware but needs new tests for new functionality.
</details>

---

### Cap 3 — Static Testing

**Q11: What types of reviews exist?**
<details>
<summary>✅ Respuesta</summary>

- **Walkthrough:** Author leads, informal, educational
- **Technical review:** Defined tech team, peer review
- **Inspection:** Most formal, moderator + roles + metrics

Each has different formality, leader, and goals.
</details>

**Q12: What's the difference between static and dynamic testing?**
<details>
<summary>✅ Respuesta</summary>

- **Static:** Without execution (reviews, static analysis)
- **Dynamic:** With execution (unit, integration, etc.)

Both find defects; static is often cheaper and finds different types.
</details>

**Q13: What's static analysis?**
<details>
<summary>✅ Respuesta</summary>

Tools that analyze code/work products without execution:
- Linting (ESLint, Pylint)
- Security scanning (Snyk, SonarQube)
- Complexity analysis
- Type checking

ISTQB recommends static + dynamic for full coverage.
</details>

---

### Cap 4 — Test Analysis & Design (the most important!)

**Q14: What are the 4 main categories of test techniques?**
<details>
<summary>✅ Respuesta</summary>

1. **Specification-based (black-box):** EP, BVA, decision tables, state transition, use case
2. **Structure-based (white-box):** Statement, branch coverage
3. **Experience-based:** Error guessing, exploratory, checklist-based
4. **Collaboration-based (NEW v4.0):** User story testing, ATDD

ISTQB v4.0.1 explicitly added collaboration-based.
</details>

**Q15: Explain Equivalence Partitioning with an example.**
<details>
<summary>✅ Respuesta</summary>

Divides inputs into groups where all values should behave the same.

Example: Age field valid 18-65
- Invalid: <18 (test with 15)
- Valid: 18-65 (test with 30)
- Invalid: >65 (test with 70)

3 tests instead of 100.
</details>

**Q16: What's the difference between BVA 2-value and 3-value?**
<details>
<summary>✅ Respuesta</summary>

- **2-value:** Test b-1, b (límite inferior); a, a+1 (límite superior)
- **3-value:** Test b-1, b, b+1, a-1, a, a+1 (agrega b+1 y a-1)

Example for 18-65:
- 2-value: 17, 18, 65, 66 (4 tests)
- 3-value: 17, 18, 19, 64, 65, 66 (6 tests, more thorough)

ISTQB v4.0.1 clarifies this distinction.
</details>

**Q17: How do you build a decision table?**
<details>
<summary>✅ Respuesta</summary>

Steps:
1. Identify conditions (inputs)
2. Identify actions (outputs)
3. List all combinations (rows)
4. Mark which actions fire for each combo
5. Collapse redundant rows

Example: Login success if user valid AND password valid AND 2FA OK. 3 conditions, 1 success + 3 fail rules = 4 rules.

Often confused with Karnaugh maps but simpler.
</details>

**Q18: What's statement vs branch coverage?**
<details>
<summary>✅ Respuesta</summary>

- **Statement coverage:** % of executable lines run
- **Branch coverage:** % of decision outcomes (true AND false) tested

Branch ≥ Statement. 100% branch often implies 100% statement.

Example: `if (x > 0) y = 1; else y = 2;`
- Statement: 1 test (x=1) → 100%
- Branch: 2 tests (x=1, x=-1) → 100%
</details>

**Q19: What's ATDD (Acceptance Test-Driven Development)?**
<details>
<summary>✅ Respuesta</summary>

Acceptance tests written BEFORE code, by team (dev + test + business).

User story → Acceptance criteria → Acceptance test → Code → Test passes

ISTQB v4.0 added this. Different from TDD (unit tests by dev).
</details>

**Q20: What's the INVEST criteria for good user stories?**
<details>
<summary>✅ Respuesta</summary>

- **I**ndependent
- **N**egotiable
- **V**aluable
- **E**stimable
- **S**mall
- **T**estable

ISTQB v4.0 includes this in Cap 4.5.
</details>

---

### Cap 5 — Managing Test Activities

**Q21: What's the difference between project risk and product risk?**
<details>
<summary>✅ Respuesta</summary>

- **Project risk:** Affects schedule/cost/quality of PROJECT (e.g., key person leaving)
- **Product risk:** Affects quality of PRODUCT (e.g., security vulnerability)

Different mitigation strategies.
</details>

**Q22: How do you calculate risk?**
<details>
<summary>✅ Respuesta</summary>

**Risk = Likelihood × Impact**

Both rated typically 1-5. Product gives 1-25 scale.

Likelihood: probability defect occurs
Impact: severity if occurs
</details>

**Q23: What are the 4 risk response strategies?**
<details>
<summary>✅ Respuesta</summary>

- **Accept:** Acknowledge but don't mitigate (low risk)
- **Mitigate:** Reduce likelihood or impact (most common)
- **Transfer:** Pass to other party (insurance, outsourcing)
- **Avoid:** Eliminate the risk entirely (don't do the feature)

ISTQB adds "share" sometimes.
</details>

**Q24: What's the test pyramid?**
<details>
<summary>✅ Respuesta</summary>

NEW in v4.0. Most tests should be at the bottom:

```
       /\
      /E2E\         ~10% (slow, expensive)
     /------\
    /Integr. \      ~20%
   /----------\
  /   Unit     \    ~70% (fast, cheap)
 /--------------\
```

Inverted pyramid = bad (slow CI, flaky tests).
</details>

**Q25: What are testing quadrants?**
<details>
<summary>✅ Respuesta</summary>

NEW in v4.0. 2x2 matrix:
- Q1 (Tech-facing, support team): Component + integration
- Q2 (Business-facing, support team): Functional, story, system
- Q3 (Business-facing, critique product): Exploratory, usability, UAT
- Q4 (Tech-facing, critique product): Performance, security, scalability

Helps teams see what types of testing they cover.
</details>

**Q26: What's the difference between severity and priority?**
<details>
<summary>✅ Respuesta</summary>

- **Severity:** Technical impact (high/medium/low)
- **Priority:** Business urgency for fixing (high/medium/low)

Example: cosmetic bug on homepage = low severity, high priority.
</details>

**Q27: What fields should a defect report have?**
<details>
<summary>✅ Respuesta</summary>

- ID, Title, Description
- Steps to reproduce
- Expected vs actual
- Severity, Priority
- Status, Assignee
- Environment (browser, OS, version)
- Attachments (screenshots, logs)
- Workaround if any
</details>

**Q28: What's the difference between test monitoring and test control?**
<details>
<summary>✅ Respuesta</summary>

- **Monitoring:** Gathering + analyzing data (measuring)
- **Control:** Taking action based on data (corrective actions)

ISTQB emphasizes this distinction (NEW v4.0 terminology).
</details>

**Q29: What are entry and exit criteria?**
<details>
<summary>✅ Respuesta</summary>

- **Entry:** Conditions to START a test level (e.g., code complete + unit tested)
- **Exit:** Conditions to STOP testing (e.g., 95% pass rate + no critical bugs)

ISTQB v4.0.1: these are NOT synonyms.
</details>

---

### Cap 6 — Test Tools

**Q30: What are categories of test tools?**
<details>
<summary>✅ Respuesta</summary>

- Test management (Jira, TestRail)
- Test execution (Selenium, Playwright)
- Performance (JMeter, k6)
- Static analysis (SonarQube, ESLint)
- Security (OWASP ZAP, Burp Suite)
- Coverage (JaCoCo, Istanbul)
- CI/CD (Jenkins, GitHub Actions)

ISTQB v4.0.1 organizes this clearly.
</details>

---

## 🛠️ SECCIÓN 2: Coding Questions (Q31-Q45)

**Q31: Write a SQL query to find duplicate emails.**
<details>
<summary>✅ Respuesta</summary>

```sql
SELECT email, COUNT(*) AS count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```
</details>

**Q32: Write Python function to check if a string is a palindrome.**
<details>
<summary>✅ Respuesta</summary>

```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```
</details>

**Q33: What is the difference between == and === in JavaScript?**
<details>
<summary>✅ Respuesta</summary>

- `==`: Loose equality (type coercion)
- `===`: Strict equality (no coercion)

Always use `===` for predictability.
</details>

**Q34: What's the difference between unit test and integration test?**
<details>
<summary>✅ Respuesta</summary>

- **Unit:** Single component isolated (no DB, no network)
- **Integration:** Multiple components together (DB calls OK, API calls OK)

Unit is fast + cheap; integration is slower + catches more.
</details>

**Q35: What's test isolation?**
<details>
<summary>✅ Respuesta</summary>

Each test should be independent — no shared state between tests.

Why: prevents flakiness, allows parallel execution, easier debugging.

Achieved with: setup/teardown, beforeEach/afterEach, fresh fixtures.
</details>

**Q36: What's mocking?**
<details>
<summary>✅ Respuesta</summary>

Replace real dependencies with fake ones for testing.

Example: Mock a payment gateway so test doesn't actually charge cards.

Tools: unittest.mock (Python), Jest mocks (JS), Mockito (Java).
</details>

**Q37: What's API testing?**
<details>
<summary>✅ Respuesta</summary>

Testing APIs directly (no UI).

Tools: Postman, Newman, REST Assured, Supertest.

Tests:
- Status codes
- Response schema
- Auth flows
- Edge cases (4xx, 5xx)
- Performance
</details>

**Q38: Explain the Page Object Model.**
<details>
<summary>✅ Respuesta</summary>

Design pattern for UI automation: each page = class with elements + actions.

Benefits:
- Maintainability (one place to update)
- Readability
- Reusability

Example: `LoginPage` class has `usernameInput`, `passwordInput`, `loginButton` and `login()` method.
</details>

**Q39: What's the difference between Selenium and Playwright?**
<details>
<summary>✅ Respuesta</summary>

| Selenium | Playwright |
|---|---|
| Older, established | Newer (Microsoft) |
| WebDriver protocol | Direct CDP |
| Slower | Faster |
| Multi-language | JS/TS/Python/Java/.NET |
| Cross-browser | Cross-browser |

Playwright is gaining market share fast in 2025.
</details>

**Q40: What's flake in testing?**
<details>
<summary>✅ Respuesta</summary>

Test that sometimes passes and sometimes fails without code changes.

Common causes:
- Race conditions
- Time dependencies
- Order dependencies
- Network issues
- Shared state

Goal: 0% flake. If >1% flake, fix or quarantine.
</details>

---

## 📊 SECCIÓN 3: Test Design Exercises (Q41-Q50)

**Q41: How would you test a login page?**
<details>
<summary>✅ Respuesta framework</summary>

Functional:
- Valid username + valid password → success
- Invalid username → error
- Invalid password → error
- Empty fields → validation
- SQL injection in fields
- Password case sensitivity

Non-functional:
- Page load time < 2s
- Concurrent logins
- Mobile responsive
- Accessibility (WCAG)

Edge cases:
- Password reset flow
- Account locked after X attempts
- 2FA flow
- "Remember me" checkbox
</details>

**Q42: You have 4 hours to test a payment system. What's your strategy?**
<details>
<summary>✅ Respuesta framework</summary>

1. **Risk-based prioritization** (30 min)
   - Critical: payment authorization
   - High: refund, cancellation
   - Medium: history view
   - Low: receipt formatting

2. **Smoke tests first** (30 min)
   - Happy path E2E

3. **Deep dive critical** (2 hours)
   - Boundary on amounts
   - Currency handling
   - Failed payment scenarios
   - Duplicate prevention

4. **Regression quick** (45 min)
   - Core flows

5. **Report + retest critical** (45 min)
</details>

**Q43: Design test cases for a coffee machine.**
<details>
<summary>✅ Respuesta</summary>

**Functional:**
- Press espresso → 30ml coffee
- Press latte → espresso + 80ml milk
- Press cappuccino → espresso + 80ml foam
- Empty water tank → error
- No beans → error
- Cup not present → warning

**Non-functional:**
- Noise < 50dB
- 1000 cycles without failure
- Cleaning cycle works

**Edge cases:**
- Power outage mid-brew
- Multiple button presses
- Foreign object in slot
</details>

**Q44: How do you decide what NOT to test?**
<details>
<summary>✅ Respuesta framework</summary>

Use risk-based + value:

- **Skip:** Low risk, low value, time-consuming
- **Test:** High risk, high value, fast feedback

Example: Don't manually test cosmetic changes vs. test core checkout flow.

Communicate trade-offs to stakeholders.
</details>

**Q45: How do you estimate testing effort?**
<details>
<summary>✅ Respuesta</summary>

Methods:
- **Expert judgment:** Senior testers estimate
- **Work breakdown:** Decompose into tasks
- **Past data:** Use velocity from previous projects
- **Three-point:** (O + 4M + P) / 6
- **Function points / use case points:** Industry-standard

ISTQB CTAL-TM covers this in detail.
</details>

---

## 💬 SECCIÓN 4: Behavioral Questions (Q46-Q60)

**Q46: Tell me about a time you found a critical bug.**
<details>
<summary>✅ Framework: STAR</summary>

**S**ituation: Payment system, 2 weeks before launch
**T**ask: Find bugs in checkout flow
**A**ction: Designed 50+ test cases including race conditions
**R**esult: Found $10M duplicate-charge bug that would have caused customer complaints

**Key:** Quantify impact + show methodology
</details>

**Q47: Tell me about a conflict with a developer.**
<details>
<summary>✅ Framework: STAR</summary>

Show how you:
- Provided evidence (logs, screenshots)
- Communicated calmly
- Found root cause together
- Focused on user impact, not blame
- Documented learning

ISTQB emphasizes collaboration over confrontation.
</details>

**Q48: Why do you want to work in QA?**
<details>
<summary>✅ Respuesta sugerida</summary>

Honest + structured:
- Passion for quality
- Mix of technical + analytical
- Visible impact on user experience
- Continuous learning
- Mention specific company/product
</details>

**Q49: What's your biggest testing failure?**
<details>
<summary>✅ Framework</summary>

Show:
- Self-awareness
- What you learned
- How you changed process after
- ISTQB principles you apply now

Example: missed a bug in prod → started using BVA + decision tables systematically.
</details>

**Q50: How do you stay current with testing trends?**
<details>
<summary>✅ Respuesta</summary>

- Ministry of Testing
- Reddit r/QualityAssurance, r/QA
- Conferences (Selenium Conf, TestBash)
- ISTQB community
- This repo 😄
- Twitter/Mastodon testing community
</details>

**Q51-Q60:** Follow-up behavioral questions covering:
- Tight deadlines
- Ambiguous requirements
- Disagreement with manager
- Estimation errors
- Working remotely
- Team conflict
- Process improvement
- Career goals
- Failure recovery
- Strengths/weaknesses

---

## 🌐 SECCIÓN 5: Resources for Interview Prep

### Repos externos (top 3)
- **Bh-bts/qa-interview-prep-resources** — 200+ Q&A
- **Devinterview-io/testing-interview-questions** — 100 fundamentals
- **shubhamagarwal1993/Interview-Questions-and-Answers** — broader

### Plataformas
- **LeetCode** — SQL + Python
- **HackerRank** — coding challenges
- **Pramp** — mock interviews
- **interviewing.io** — technical mock
- **Exercism** — language practice

### Tools para practicar
- **Postman** — API testing
- **SQLBolt** — SQL practice
- **OWASP WebGoat** — security practice
- **SauceLabs / BrowserStack** — cross-browser

---

## 🎯 Final Tips

### Antes de la interview

- [ ] Investigá la empresa (product, tech stack, recent news)
- [ ] Repasá tu portfolio / proyectos
- [ ] Practicá inglés (si aplica)
- [ ] Dormí bien, comé, hidratate

### Durante

- [ ] Hacé preguntas (mostrar interés)
- [ ] Pensá en voz alta (mostrar proceso)
- [ ] Si no sabés algo, decilo (no inventes)
- [ ] Pedí clarificación si la pregunta es ambigua
- [ ] Usá ejemplos concretos (no abstractos)

### Después

- [ ] Mandá thank-you email (24h)
- [ ] Pedí feedback si rechazan
- [ ] Documentá learnings para la próxima
- [ ] Network: conectá en LinkedIn con el interviewer

---

## 📊 Quick Reference Card (1 página)

Print this and review before each interview:

```
ISTQB CORE CONCEPTS — KNOW THESE COLD
──────────────────────────────────────
• 7 testing principles
• Test pyramid (70% unit / 20% integration / 10% E2E)
• Testing quadrants (Q1-Q4)
• EP / BVA 2-value + 3-value / Decision tables / State
• Statement vs branch coverage
• Severity vs priority
• Project risk vs product risk
• Risk = likelihood × impact
• Static vs dynamic
• Verification vs validation
• Regression vs confirmation
• ATDD vs TDD
• INVEST criteria

CODING — PRACTICE WEEKLY
────────────────────────
• SQL basics (joins, group by, having)
• Python or JS basics
• API testing with Postman
• Git basics

BEHAVIORAL — STAR
─────────────────
S: Situation (context)
T: Task (your responsibility)
A: Action (what you did)
R: Result (measurable impact)
```

---

## ✅ Self-Assessment

| Score | Estado |
|---|---|
| 50-60 (80%+) | Listo para senior roles |
| 40-49 (65-80%) | Listo para mid roles |
| 30-39 (50-65%) | Listo para junior roles |
| <30 | Más preparación necesaria |

---

## 🔗 Para profundizar

- **bh-bts/qa-interview-prep-resources:** https://github.com/Bh-bts/qa-interview-prep-resources
- **devinterview-io:** https://github.com/Devinterview-io/testing-interview-questions
- **FAQGURU:** https://github.com/FAQGURU/FAQGURU

**Recordá:** ISTQB es la base. Coding + portfolio + inglés = interview-ready.
