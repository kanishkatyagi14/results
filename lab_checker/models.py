"""Task 3: Classes for patients, lab results and reference ranges.

Fill in each class so the tests in tests/test_task3_models.py pass.
"""


class Patient:
    def __init__(self, patient_id, name, age, sex):
        # TODO: Task 3 - store all four values as attributes.
        # age may arrive as text ("58"); always store it as an int.
        raise NotImplementedError("Task 3: Patient.__init__")

    @classmethod
    def from_row(cls, row):
        """Build a Patient from one dict returned by load_csv()."""
        # TODO: Task 3
        raise NotImplementedError("Task 3: Patient.from_row")

    def is_senior(self):
        """Return True if the patient is 60 or older."""
        # TODO: Task 3
        raise NotImplementedError("Task 3: Patient.is_senior")


class LabResult:
    def __init__(self, result_id, patient_id, test_code, value, unit, collected_on):
        # TODO: Task 3 - store all six values as attributes.
        # Keep `value` as the RAW TEXT. Do not convert it here.
        raise NotImplementedError("Task 3: LabResult.__init__")

    @classmethod
    def from_row(cls, row):
        # TODO: Task 3
        raise NotImplementedError("Task 3: LabResult.from_row")


class ReferenceRange:
    def __init__(self, test_code, test_name, sex, low, high, unit,
                 critical_low=None, critical_high=None):
        # TODO: Task 3 - store all values as attributes.
        # low and high must be floats. critical_low / critical_high are floats or None.
        raise NotImplementedError("Task 3: ReferenceRange.__init__")

    @classmethod
    def from_row(cls, row):
        """Build from a CSV row. An EMPTY critical_low / critical_high cell becomes None."""
        # TODO: Task 3
        raise NotImplementedError("Task 3: ReferenceRange.from_row")

    def applies_to(self, sex):
        """True if this range is for everyone (sex "A") or matches the given sex ("M"/"F")."""
        # TODO: Task 3
        raise NotImplementedError("Task 3: ReferenceRange.applies_to")
