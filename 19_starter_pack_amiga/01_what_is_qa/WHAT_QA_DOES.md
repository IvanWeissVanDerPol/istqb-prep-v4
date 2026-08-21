# 🐛 What does a QA Tester actually do?

*Made for you, with love — a beginner's guide that uses what you already know*

---

## 🌟 Start here

You asked *"what is QA?"* — let me show you something first.

**You already think like a QA tester.** You just don't call it that yet.

Every day, with the animals you care for, you do things a QA tester does:

| What you already do (with animals) | What a QA tester does (with apps) |
|---|---|
| 🐍 Notice a snake's shed looks incomplete | Notice a button on a screen doesn't work |
| 🦜 Watch if a parrot's eating less than normal | Watch if an app crashes when you tap a button |
| 🐕 Track exact medication doses per animal | Track exact reproduction steps for a bug |
| 🐢 Spot when the humidity is wrong in the terrarium | Spot when the app behaves wrong on a specific phone |
| 📋 Keep records: weight, food, behavior | Keep records: bug reports, screenshots, steps |
| 🔍 Look for tiny details others miss | Look for tiny details others miss |

**That's it.** A QA tester is a *professional bug-spotter for apps*. You use the app carefully, find what doesn't work, write a clear report, and the developers fix it.

That's the whole job in one sentence.

---

## 🎯 The job, in plain English

A company builds an app (could be a banking app, a delivery app, a game, anything).

**Before the app goes live**, the company needs someone to:

1. **Click through everything** the user would do
2. **Find things that are broken** — buttons that crash, wrong numbers, ugly screens
3. **Write a clear report** explaining exactly how to reproduce the bug
4. **Re-test after the fix** — make sure they really fixed it AND didn't break something else

That's it. **No programming required to start.**

---

## 🐛 A real example you'll do on day 1

Imagine you're testing a food delivery app like PedidosYa.

You open it on your iPhone and start clicking:

| You try this | What's supposed to happen | What actually happens | You write |
|---|---|---|---|
| Tap "Add to cart" | Item appears in cart | Item appears ✓ | (no bug) |
| Add 99 of the same item | Shows 99 in cart | Shows "—" (blank!) | 🐛 Bug |
| Place order with no internet | Says "no internet, try again" | Crashes the whole app | 🐛 Major bug |
| Change language to Guaraní | Everything in Guaraní | "Submit" button still English | 🐛 Bug |
| Try a coupon from 2019 | Says "expired" | Says "applied! 50% off" | 🐛 Bug |

Every line in that right column is a **bug report**. Your job is to find these and write them down clearly enough that a developer can fix it without asking you a single question.

**Notice what the job ISN'T:** You're not the one fixing the bug. You're not writing code. You're not designing the app. You're the *quality detective*.

---

## 🐾 Why you're already qualified

You care for exotic animals — let me tell you what that proves:

### 1. **You notice when something is "off"**

A snake's humidity is at 78% but you can tell it's *drying out faster than usual this week*. An app developer looks at a screen and says "looks fine to me." You look at the same screen and notice the text is *slightly* clipped on the right edge.

**That's the skill.** Most people can't do this. You already do it every day.

### 2. **You write down exact details**

"When did the iguana last eat? What did it eat? Was it normal?" → bug report format:
- **Steps:** Fed iguana lettuce at 9am
- **Expected:** Eats normally
- **Actual:** Refused food, was less active after

You're already writing bug reports. You just call them "animal care notes."

### 3. **You handle different "environments"**

Desert terrarium ≠ tropical vivarium ≠ saltwater tank. Each animal needs different conditions.

In QA, you test:
- iPhone vs Android
- Wi-Fi vs mobile data
- New user vs logged-in user
- Spanish vs English

**Same skill.** Different environment.

### 4. **You don't panic when something is broken**

A sick animal needs calm, methodical observation. Not "OMG SOMETHING IS WRONG." Same with bugs. Calm, clear, documented.

---

## � What a typical day looks like

For a junior QA tester (your first job, in ~6-12 months):

```
9:00 AM  →  Stand-up meeting (15 min, on Zoom) — what you'll test today
9:15 AM  →  Read what changed in the app (the "new stuff to test")
10:00 AM →  Test on iPhone, iPad, Android, computer — find bugs
12:00 PM →  Lunch
1:00 PM  →  Write up the bugs you found (clear reports with screenshots)
2:30 PM  →  Check the bugs the developers fixed yesterday — confirm they work
3:30 PM  →  Test the new feature the team just built
5:00 PM  →  Wrap up notes for tomorrow, log off
```

**That's a real day.** Notice: no math, no programming, no late nights, no "saving lives" pressure. Just careful, focused testing.

---

## 🤔 "But I don't know code!"

**You don't need to. Not for the first 6-12 months.**

QA work has levels:

| Level | What's needed | Salary range (USD/year) |
|---|---|---|
| � **Manual QA** (you start here) | No code. Just careful clicking & writing. | $24,000 - $48,000 remote |
| 🟡 **Test Automation** (after 6-12 months) | Learn Python or JavaScript, basics | $48,000 - $84,000 remote |
| 🔴 **Senior SDET** (after 2-3 years) | Build automation frameworks | $80,000 - $140,000 remote |

You start at 🟢. You grow into the others. **The first job is the door. Not the ceiling.**

---

## 🌍 Why this career is special right now

1. **Demand is exploding.** The US government says QA jobs will grow 25% by 2032 (Bureau of Labor Statistics). There are more jobs than people to fill them.
2. **Remote is normal now.** Companies in the US, EU, UK will hire you from your apartment in Asunción. They pay you in dollars. You keep living where you live.
3. **AI is making it MORE important, not less.** "But won't AI replace QA?" → No. AI generates code *faster*, which means *more bugs to find*. AI is your tool, not your replacement.
4. **Your detail-orientation is rare.** Most people hate this work. People who are good at it (like you, with animals) are in demand.

---

## 🧠 The vocabulary you'll hear (in plain English)

When you start, people will use words. Don't panic:

| Word | What it means |
|---|---|
| **Bug / Defect** | Something broken in the app |
| **Test case** | A checklist of things to check |
| **Regression** | Re-test everything to make sure nothing broke |
| **Staging / Production** | Staging = fake app for testing. Production = real app users see |
| **Sprint** | A 2-week chunk of work |
| **Jira / Azure DevOps** | Where you write bug reports |
| **Severity** | How bad the bug is (cosmetic? crash?) |
| **Priority** | How fast to fix it |
| **Smoke test** | Quick "is the app even alive" check |
| **Exploratory testing** | Click around freely without a script |
| **Test plan** | The document saying "what we're testing and how" |

Don't memorize. You'll learn by doing.

---

## 🎯 Your first goal (concrete and small)

Before any of the salary stuff or job hunting, your **only goal for the next 6-8 weeks** is:

> **Pass the ISTQB CTFL exam.**

It's an international certificate that:
- Proves you know the basics
- Looks good on your CV/resume
- Costs about USD 200 in Paraguay
- Has 40 multiple-choice questions
- 65% to pass (26 out of 40)
- Valid forever

There's a full guide to that in `02_study_plan/`. Don't worry about it yet. Just know that's step 1.

After that:
- Step 2: Learn basics of automation (3-6 months)
- Step 3: First job (manual QA, remote or local)
- Step 4: Keep learning automation
- Step 5: Bigger salary

We'll walk through each step.

---

## 💬 A note from your friend who wrote this

You already have the hardest part: **the eye for detail, the patience to be thorough, and the calm to write things down clearly when something is wrong.**

Software testers do exactly that, but for apps instead of animals. You're not learning a new skill — you're *transferring* one you already have.

The tech part is learnable. The detail part is a gift.

---

## 📂 Next file to read

→ `02_study_plan/ISTQB_PLAN_FOR_YOU.md` — your personal 6-week study plan

*If anything in here felt confusing, ask your friend and we'll explain it in a different way.*
