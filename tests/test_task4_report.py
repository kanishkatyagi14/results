"""Task 4 tests: checking all results and building the report."""

import csv
import os

import pytest

from lab_checker.loader import load_csv
from lab_checker.models import Patient, LabResult, ReferenceRange
from lab_checker.checker import find_range, check_results
from lab_checker.report import summarize, flagged_only, write_flagged_csv

DATA = os.path.join(os.path.dirname(__file__), "..", "data")


@pytest.fixture
def loaded():
    patients = [Patient.from_row(r) for r in load_csv(os.path.join(DATA, "patients.csv"))]
    results = [LabResult.from_row(r) for r in load_csv(os.path.join(DATA, "lab_results.csv"))]
    ranges = [ReferenceRange.from_row(r) for r in load_csv(os.path.join(DATA, "reference_ranges.csv"))]
    return patients, results, ranges


@pytest.fixture
def checked(loaded):
    patients, results, ranges = loaded
    return check_results(patients, results, ranges)


def flag_of(checked, result_id):
    return [row for row in checked if row["result_id"] == result_id][0]["flag"]


# ---- find_range ----

def test_find_range_uses_sex(loaded):
    _, _, ranges = loaded
    assert find_range(ranges, "HGB", "F").low == 12.0
    assert find_range(ranges, "HGB", "M").low == 13.5


def test_find_range_all_sexes(loaded):
    _, _, ranges = loaded
    assert find_range(ranges, "K", "F").low == 3.5


def test_find_range_unknown_test(loaded):
    _, _, ranges = loaded
    assert find_range(ranges, "VITD", "F") is None


# ---- check_results ----

def test_one_row_per_result_in_order(checked):
    assert len(checked) == 32
    assert checked[0]["result_id"] == "R001"
    assert checked[-1]["result_id"] == "R032"


def test_row_has_patient_name(checked):
    assert checked[0]["patient_name"] == "Asha Verma"


@pytest.mark.parametrize("result_id, expected", [
    ("R001", "LOW"),            # HGB 11.2, female
    ("R004", "HIGH"),           # TSH 5.6
    ("R006", "HIGH"),           # GLU 182
    ("R009", "CRITICAL_LOW"),   # HGB 6.4
    ("R011", "CRITICAL_HIGH"),  # K 6.9
    ("R013", "NORMAL"),         # HGB 13.5 male, exactly the low limit
    ("R016", "INVALID"),        # empty value
    ("R017", "NORMAL"),         # HGB 13.0 female (would be LOW for a male!)
    ("R020", "UNKNOWN_TEST"),   # VITD has no reference range
    ("R021", "CRITICAL_LOW"),   # GLU 45
    ("R026", "CRITICAL_LOW"),   # PLT 15
    ("R027", "INVALID"),        # "N/A"
    ("R028", "NORMAL"),         # "  88 " with spaces
    ("R031", "UNKNOWN_PATIENT"),  # P009 is not in patients.csv
])
def test_flags(checked, result_id, expected):
    assert flag_of(checked, result_id) == expected


# ---- report ----

def test_summarize(checked):
    counts = summarize(checked)
    assert sum(counts.values()) == 32
    assert counts["NORMAL"] == 16
    assert counts["CRITICAL_LOW"] == 3
    assert counts["UNKNOWN_PATIENT"] == 1


def test_flagged_only_drops_normal(checked):
    flagged = flagged_only(checked)
    assert len(flagged) == 16
    assert all(row["flag"] != "NORMAL" for row in flagged)


def test_write_flagged_csv(checked, tmp_path):
    out = tmp_path / "flagged.csv"
    write_flagged_csv(checked, out)
    with open(out, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 16
    assert rows[0]["result_id"] == "R001"
    assert rows[0]["flag"] == "LOW"
    assert "patient_name" in rows[0]
