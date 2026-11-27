# Lab Result Checker – Week 1 Notes

### 1. Why does R017 (Hemoglobin 13.0, female) come out NORMAL, when 13.0 would be LOW for a male?

Because the reference ranges depend on the patient's sex. For females, the range is 12–15.5 g/dL, so 13.0 is NORMAL. For males, the range is 13.5–17.5 g/dL, so 13.0 would be LOW.

### 2. Why should a value exactly equal to the high limit be NORMAL and not HIGH?

Because the reference range includes both its lower and upper limits. A value equal to the upper limit is still within the normal range. Only a value greater than the upper limit should be classified as HIGH.

### 3. Pick one CRITICAL_* result. What could happen if our software showed it as just LOW?

For example, R011 has potassium of 6.9 mmol/L and is classified as CRITICAL_HIGH. If it were shown as just HIGH or LOW, its urgency might not be recognized. This could delay medical attention for a potentially dangerous condition.

### 4. What was the hardest part of this week, and how did you solve it?

The hardest part was understanding how different Python files and classes work together. I solved it by reading the docstrings, understanding each function, implementing tasks step by step, and running pytest after completing each task.

### 5. One question you still have.

How can we maintain and update reference ranges for different tests, age groups, and patient categories in a real Laboratory Information System (LIS)?

