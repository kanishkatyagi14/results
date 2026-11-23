"""Task 1: Read CSV files into Python lists."""

import csv  # noqa: F401  (you will need this)


def load_csv(path):
    """Read a CSV file and return a list of dictionaries, one per row.

    - Keys are the column names from the header row.
    - Values are strings, with leading/trailing spaces removed.
    - An empty cell becomes an empty string "".

    Example:
        rows = load_csv("data/patients.csv")
        rows[0]  ->  {"patient_id": "P001", "name": "Asha Verma", "age": "34", "sex": "F"}

    Hint: look up csv.DictReader and the "with open(...)" pattern.
    """
    # TODO: Task 1
    raise NotImplementedError("Task 1: write load_csv")
