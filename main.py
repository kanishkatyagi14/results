"""Run the Lab Result Checker from the command line.

    python main.py
    python main.py --flagged-only --out output/flagged.csv
"""

import argparse
import os

from lab_checker.loader import load_csv
from lab_checker.models import Patient, LabResult, ReferenceRange
from lab_checker.checker import check_results
from lab_checker.report import summarize, flagged_only, format_line, write_flagged_csv


def main():
    parser = argparse.ArgumentParser(description="Flag lab results as LOW / NORMAL / HIGH.")
    parser.add_argument("--data", default="data", help="folder with the CSV files")
    parser.add_argument("--flagged-only", action="store_true", help="print only non-NORMAL results")
    parser.add_argument("--out", help="write flagged results to this CSV file")
    args = parser.parse_args()

    patients = [Patient.from_row(r) for r in load_csv(os.path.join(args.data, "patients.csv"))]
    results = [LabResult.from_row(r) for r in load_csv(os.path.join(args.data, "lab_results.csv"))]
    ranges = [ReferenceRange.from_row(r) for r in load_csv(os.path.join(args.data, "reference_ranges.csv"))]

    checked = check_results(patients, results, ranges)
    rows = flagged_only(checked) if args.flagged_only else checked

    print("LAB RESULT CHECK - TRAINING DATA ONLY")
    print("=" * 80)
    for row in rows:
        print(format_line(row))
    print("=" * 80)
    print("Summary:")
    for flag, count in sorted(summarize(checked).items()):
        print(f"  {flag:<16} {count}")

    if args.out:
        folder = os.path.dirname(args.out)
        if folder:
            os.makedirs(folder, exist_ok=True)
        write_flagged_csv(checked, args.out)
        print(f"\nFlagged results written to {args.out}")


if __name__ == "__main__":
    main()
