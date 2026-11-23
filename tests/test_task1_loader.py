"""Task 1 tests: reading CSV files."""

import os

from lab_checker.loader import load_csv

DATA = os.path.join(os.path.dirname(__file__), "..", "data")


def test_loads_all_patients():
    rows = load_csv(os.path.join(DATA, "patients.csv"))
    assert len(rows) == 8


def test_rows_are_dicts_with_header_keys():
    rows = load_csv(os.path.join(DATA, "patients.csv"))
    first = rows[0]
    assert isinstance(first, dict)
    assert first["patient_id"] == "P001"
    assert first["name"] == "Asha Verma"
    assert first["sex"] == "F"


def test_loads_all_results():
    rows = load_csv(os.path.join(DATA, "lab_results.csv"))
    assert len(rows) == 32


def test_values_are_stripped_of_spaces():
    rows = load_csv(os.path.join(DATA, "lab_results.csv"))
    r028 = [r for r in rows if r["result_id"] == "R028"][0]
    assert r028["value"] == "88"


def test_empty_cell_becomes_empty_string():
    rows = load_csv(os.path.join(DATA, "lab_results.csv"))
    r016 = [r for r in rows if r["result_id"] == "R016"][0]
    assert r016["value"] == ""
