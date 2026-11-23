"""Task 3 tests: Patient, LabResult and ReferenceRange classes."""

from lab_checker.models import Patient, LabResult, ReferenceRange


def test_patient_basic():
    p = Patient("P001", "Asha Verma", 34, "F")
    assert p.patient_id == "P001"
    assert p.name == "Asha Verma"
    assert p.age == 34
    assert p.sex == "F"


def test_patient_age_from_text_becomes_int():
    p = Patient("P002", "Rohan Mehta", "58", "M")
    assert p.age == 58


def test_patient_from_row():
    row = {"patient_id": "P003", "name": "Fatima Khan", "age": "71", "sex": "F"}
    p = Patient.from_row(row)
    assert p.patient_id == "P003"
    assert p.age == 71


def test_patient_is_senior():
    assert Patient("P003", "Fatima Khan", 71, "F").is_senior() is True
    assert Patient("P006", "Arjun Nair", 60, "M").is_senior() is True
    assert Patient("P001", "Asha Verma", 34, "F").is_senior() is False


def test_lab_result_from_row_keeps_raw_value():
    row = {"result_id": "R027", "patient_id": "P007", "test_code": "WBC",
           "value": "N/A", "unit": "10^3/uL", "collected_on": "2026-11-19"}
    r = LabResult.from_row(row)
    assert r.result_id == "R027"
    assert r.test_code == "WBC"
    assert r.value == "N/A"


def test_reference_range_from_row_converts_numbers():
    row = {"test_code": "K", "test_name": "Potassium", "sex": "A", "low": "3.5",
           "high": "5.1", "unit": "mmol/L", "critical_low": "2.5", "critical_high": "6.5"}
    rng = ReferenceRange.from_row(row)
    assert rng.low == 3.5
    assert rng.high == 5.1
    assert rng.critical_low == 2.5
    assert rng.critical_high == 6.5


def test_reference_range_empty_critical_is_none():
    row = {"test_code": "TSH", "test_name": "Thyroid Stimulating Hormone", "sex": "A",
           "low": "0.4", "high": "4.0", "unit": "mIU/L", "critical_low": "", "critical_high": ""}
    rng = ReferenceRange.from_row(row)
    assert rng.critical_low is None
    assert rng.critical_high is None


def test_reference_range_applies_to():
    all_sexes = ReferenceRange("K", "Potassium", "A", 3.5, 5.1, "mmol/L")
    female = ReferenceRange("HGB", "Hemoglobin", "F", 12.0, 15.5, "g/dL")
    assert all_sexes.applies_to("M") is True
    assert all_sexes.applies_to("F") is True
    assert female.applies_to("F") is True
    assert female.applies_to("M") is False
