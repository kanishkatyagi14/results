# Week 1 Assignment: Lab Result Checker

Welcome to the team! This week you'll build a small Python program that does what our
lab systems do every day: **take lab results, compare them to normal ranges, and flag
anything abnormal.**

> **Training data only.** All patients in `data/` are made up. The reference ranges are
> simplified for learning and must **not** be used for real patients.

---

## What you'll build

A command-line program that reads three CSV files and prints a report like this:

```
R001  P001  Asha Verma      HGB      11.2 g/dL      (12-15.5)     LOW
R009  P003  Fatima Khan     HGB       6.4 g/dL      (12-15.5)     CRITICAL_LOW
R016  P004  Vikram Singh    PLT         - 10^3/uL   (150-450)     INVALID
...
Summary:
  CRITICAL_HIGH    1
  CRITICAL_LOW     3
  ...
```

### The data

| File | What's in it |
| --- | --- |
| `data/patients.csv` | 8 patients: ID, name, age, sex |
| `data/lab_results.csv` | 32 test results, as if sent by a lab machine |
| `data/reference_ranges.csv` | Normal range and critical limits for each test (some differ by sex) |

Watch out: the results file has **messy data on purpose** — empty values, `N/A`, extra
spaces, a test with no range, and a patient who doesn't exist. Real machine data looks
like this too.

### The flags

| Flag | Meaning |
| --- | --- |
| `NORMAL` | Between low and high (limits included) |
| `LOW` / `HIGH` | Outside the normal range |
| `CRITICAL_LOW` / `CRITICAL_HIGH` | Dangerously outside — in a real lab the doctor is called immediately |
| `INVALID` | Value is empty or not a number |
| `UNKNOWN_TEST` | No reference range for this test |
| `UNKNOWN_PATIENT` | Patient ID not found |

---

## Setup (Day 1)

```bash
git clone <this-repo-url>
cd week1-lab-result-checker
python -m venv .venv
# Windows:  .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
git checkout -b week1/<your-name>
```

Run the tests (they will all fail at first — that's expected):

```bash
pytest
```

---

## Tasks

Do them in order. Each task has its own test file. **A task is done when its tests pass.**

| Day | Task | File(s) to edit | Check with |
| --- | --- | --- | --- |
| Tue | **1. Read CSV files** — write `load_csv()` | `lab_checker/loader.py` | `pytest tests/test_task1_loader.py` |
| Wed | **2. Flag a value** — write `parse_value()` and `classify()` | `lab_checker/checker.py` | `pytest tests/test_task2_classify.py` |
| Thu | **3. Classes** — complete `Patient`, `LabResult`, `ReferenceRange` | `lab_checker/models.py` | `pytest tests/test_task3_models.py` |
| Thu–Fri | **4. Check everything + report** — `find_range()`, `check_results()`, `summarize()`, `flagged_only()`, `write_flagged_csv()` | `lab_checker/checker.py`, `lab_checker/report.py` | `pytest tests/test_task4_report.py` |
| Fri | **5. Run it and open a pull request** | — | see below |

Every function has a docstring that explains exactly what it must do, with hints.
Read it first.

### Task 5: Run it and submit

When all tests pass:

```bash
pytest                                    # all green
python main.py                            # full report
python main.py --flagged-only             # only problems
python main.py --out output/flagged.csv   # save flagged results to a file
```

Then:

1. Write `NOTES.md` (see below).
2. Push your branch and open a **Pull Request** into `main`.
3. Fill in the PR checklist. Your mentor will review it.

---

## NOTES.md (write this yourself)

Create `NOTES.md` in the repo with short answers:

1. Why does `R017` (Hemoglobin 13.0, female) come out NORMAL, when 13.0 would be LOW for a male?
2. Why should a value exactly equal to the high limit be NORMAL and not HIGH?
3. Pick one `CRITICAL_*` result. What could happen if our software showed it as just `LOW`?
4. What was the hardest part of this week, and how did you solve it?
5. One question you still have.

---

## Rules

- **Small commits, clear messages.** At least one commit per task, e.g. `Task 2: add classify with critical limits`.
  Aim for 5+ commits.
- **Don't edit the tests or the data files** to make tests pass.
- **Don't push to `main`.** Work on your branch and open a PR.
- **Stuck for 30 minutes?** Ask your mentor. That's what they're for.
- Using AI tools or Google is fine for learning, but you must be able to explain every line you submit.

## Bonus (only after everything else passes)

- [ ] Add `--patient P003` to print only one patient's results.
- [ ] Print a per-patient report: name, age, then their results, with `!!` next to critical values.
- [ ] Check that the result's unit matches the range's unit; flag `UNIT_MISMATCH` if not (write your own test).
- [ ] Mark seniors (60+) in the report using `Patient.is_senior()`.

## Why this matters

Our Lab Management System and Veterinary LMS receive results from analyser machines and
must flag abnormal and critical values correctly before a report reaches a doctor. This
assignment is a small version of that exact job.
