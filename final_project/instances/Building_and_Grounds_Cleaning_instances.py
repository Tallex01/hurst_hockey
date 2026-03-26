import csv
from pathlib import Path
from models import Building_and_Grounds_Cleaning


def _to_int(value):
    if value is None:
        return None
    text = str(value).strip()
    if not text or text.upper() == "NA":
        return None
    try:
        return int(text.replace(",", ""))
    except ValueError:
        return None


def create_building_and_grounds_cleaning_instances():
    """
    Read Building_and_Grounds_Cleaning.csv and create a list of Building_and_Grounds_Cleaning instances.

    Returns:
        list: A list of Building_and_Grounds_Cleaning objects populated from the CSV file
    """
    instances = []
    csv_path = Path(__file__).resolve().parent.parent / "groups" / "Building_and_Grounds_Cleaning.csv"

    with csv_path.open('r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            instance = Building_and_Grounds_Cleaning(
                job_name=row.get('job_name') or None,
                job_group=row.get('job_group') or None,
                annual_openings=_to_int(row.get('annual_openings')),
                med_annual_pay=_to_int(row.get('med_annual_pay')),
                entry_lvl_ed=row.get('entry_lvl_ed') or None,
            )
            instances.append(instance)

    return instances
