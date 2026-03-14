import csv
from pathlib import Path
from models import Groups


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


def create_group_instances():
    """
    Read groups.csv and create a list of Groups instances.

    Returns:
        list: A list of Groups objects populated from groups.csv
    """
    group_list = []
    csv_path = Path(__file__).resolve().parent / 'groups.csv'

    with csv_path.open('r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            group = Groups(
                job_group=row.get('job_group') or None,
                annual_openings=_to_int(row.get('annual_openings')),
                med_annual_pay=_to_int(row.get('med_annual_pay')),
            )
            group_list.append(group)

    return group_list
