
"""Task 3: Classes for patients, lab results and reference ranges."""


class Patient:
    def __init__(self, patient_id, name, age, sex):
        self.patient_id = patient_id
        self.name = name
        self.age = int(age)
        self.sex = sex

    @classmethod
    def from_row(cls, row):
        """Build a Patient from one dict returned by load_csv()."""
        return cls(
            row["patient_id"],
            row["name"],
            row["age"],
            row["sex"]
        )

    def is_senior(self):
        """Return True if the patient is 60 or older."""
        return self.age >= 60


class LabResult:
    def __init__(self, result_id, patient_id, test_code, value, unit, collected_on):
        self.result_id = result_id
        self.patient_id = patient_id
        self.test_code = test_code
        self.value = value
        self.unit = unit
        self.collected_on = collected_on

    @classmethod
    def from_row(cls, row):
        return cls(
            row["result_id"],
            row["patient_id"],
            row["test_code"],
            row["value"],
            row["unit"],
            row["collected_on"]
        )


class ReferenceRange:
    def __init__(self, test_code, test_name, sex, low, high, unit,
                 critical_low=None, critical_high=None):

        self.test_code = test_code
        self.test_name = test_name
        self.sex = sex
        self.low = float(low)
        self.high = float(high)
        self.unit = unit

        self.critical_low = (
            float(critical_low) if critical_low not in (None, "") else None
        )

        self.critical_high = (
            float(critical_high) if critical_high not in (None, "") else None
        )

    @classmethod
    def from_row(cls, row):
        """Build from a CSV row."""
        return cls(
            row["test_code"],
            row["test_name"],
            row["sex"],
            row["low"],
            row["high"],
            row["unit"],
            row["critical_low"],
            row["critical_high"]
        )

    def applies_to(self, sex):
        """True if range is for everyone or matches the given sex."""
        return self.sex == "A" or self.sex == sex
