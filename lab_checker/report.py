"""Task 4: Turn checked results into a readable report."""

import csv  # noqa: F401  (you will need this)

from lab_checker.checker import NORMAL  # noqa: F401

FLAGGED_COLUMNS = ["result_id", "patient_id", "patient_name", "test_code",
                   "value", "unit", "low", "high", "flag"]


def summarize(checked):
    """Count how many results got each flag."""

    counts = {}

    for row in checked:
        flag = row["flag"]

        if flag not in counts:
            counts[flag] = 0

        counts[flag] += 1

    return counts
    """
        summarize(checked) -> {"NORMAL": 16, "LOW": 5, ...}
    """
    # TODO: Task 4
  


def flagged_only(checked):
    """Return only the rows whose flag is NOT NORMAL (keep the same order)."""
    # TODO: Task 4
    return [
        row for row in checked
        if row["flag"] != NORMAL
    ]
    



def write_flagged_csv(checked, path):
    """Write the non-NORMAL rows to a CSV file."""

    flagged = flagged_only(checked)

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=FLAGGED_COLUMNS
        )

        writer.writeheader()
        writer.writerows(flagged)

    """Write the non-NORMAL rows to a CSV file.

    - Header = FLAGGED_COLUMNS
    - A None value is written as an empty cell.

    Hint: csv.DictWriter
    """
    # TODO: Task 4
   


# ------------------------------------------------------------------
# Given to you - no need to change this.

def format_line(row):
    """One line of the printed report."""
    value = "-" if row["value"] is None else f"{row['value']:g}"
    if row["low"] is None:
        ref = "(no range)"
    else:
        ref = f"({row['low']:g}-{row['high']:g})"
    return (f"{row['result_id']:<5} {row['patient_id']:<5} {row['patient_name']:<15} "
            f"{row['test_code']:<6} {value:>6} {row['unit']:<9} {ref:<13} {row['flag']}")
