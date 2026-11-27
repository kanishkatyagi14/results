"""Task 2 and Task 4: Check each result against its reference range."""

# Use these constants instead of typing the strings each time.
LOW = "LOW"
NORMAL = "NORMAL"
HIGH = "HIGH"
CRITICAL_LOW = "CRITICAL_LOW"
CRITICAL_HIGH = "CRITICAL_HIGH"
INVALID = "INVALID"
UNKNOWN_TEST = "UNKNOWN_TEST"
UNKNOWN_PATIENT = "UNKNOWN_PATIENT"


# ---------------------------------------------------------------- Task 2

def parse_value(raw):
    """Turn raw text into a float.

    Return None if raw is None, empty, only spaces, or not a number (e.g. "N/A").

        parse_value("11.2")  -> 11.2
        parse_value("  88 ") -> 88.0
        parse_value("N/A")   -> None

    Hint: float() raises ValueError on bad text. Use try/except.
    """
    # TODO: Task 2
    try:
        return float(raw)
    except (ValueError, TypeError):
        return None


def classify(value, low, high, critical_low=None, critical_high=None):
    """Return the flag for a numeric value.

    Rules, checked in this order:
      1. critical_low given and value <  critical_low  -> CRITICAL_LOW
      2. critical_high given and value > critical_high -> CRITICAL_HIGH
      3. value <  low  -> LOW
      4. value >  high -> HIGH
      5. otherwise     -> NORMAL   (so a value EQUAL to low or high is NORMAL)
    """
    # TODO: Task 2
    if critical_low is not None and value < critical_low:
        return CRITICAL_LOW

    if critical_high is not None and value > critical_high:
        return CRITICAL_HIGH

    if value < low:
        return LOW

    if value > high:
        return HIGH

    return NORMAL


# ---------------------------------------------------------------- Task 4

def find_range(ranges, test_code, sex):
    """Return the matching ReferenceRange, or None."""

    for reference_range in ranges:
        if (
            reference_range.test_code == test_code
            and reference_range.applies_to(sex)
        ):
            return reference_range

    return None
    """Return the ReferenceRange in `ranges` for this test_code and sex, or None.

    A range with sex "A" applies to everyone. Use ReferenceRange.applies_to().
    """




def check_results(patients, results, ranges):
    """Check every LabResult and return checked rows."""

    # Create a dictionary for quick patient lookup
    patient_dict = {
        patient.patient_id: patient
        for patient in patients
    }

    checked = []

    for result in results:

        # Find the patient
        patient = patient_dict.get(result.patient_id)

        # Convert raw value into a number
        value = parse_value(result.value)

        low = None
        high = None

        if patient is None:
            flag = UNKNOWN_PATIENT

        else:
            reference_range = find_range(
                ranges,
                result.test_code,
                patient.sex
            )

            if reference_range is None:
                flag = UNKNOWN_TEST

            else:
                low = reference_range.low
                high = reference_range.high

                if value is None:
                    flag = INVALID
                else:
                    flag = classify(
                        value,
                        low,
                        high,
                        reference_range.critical_low,
                        reference_range.critical_high
                    )

        checked.append({
            "result_id": result.result_id,
            "patient_id": result.patient_id,
            "patient_name": patient.name if patient else "",
            "test_code": result.test_code,
            "value": value,
            "unit": result.unit,
            "low": low,
            "high": high,
            "flag": flag
        })

    return checked

    """Check every LabResult. Return a list of dicts, one per result, SAME ORDER as `results`.

    Each dict has these keys:
        result_id, patient_id, patient_name, test_code,
        value  (float, or None if it could not be parsed),
        unit, low, high  (None if no range was found),
        flag

    How to pick the flag:
        - patient_id not found in patients         -> UNKNOWN_PATIENT
        - no reference range for this test and sex -> UNKNOWN_TEST
        - value could not be parsed                -> INVALID
        - otherwise                                -> classify(...)

    Hint: build a dict {patient_id: Patient} first, so lookups are fast.
    """
    # TODO: Task 4
    
