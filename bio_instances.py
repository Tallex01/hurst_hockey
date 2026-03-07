import csv
from models import Bio


def create_bio_instances():
    """
    Read the bio.csv file and create a list of Bio instances.
    
    Returns:
        list: A list of Bio objects populated from the bio.csv file
    """
    bio_list = []
    
    with open('bio.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Convert jersey_number to int, handling None/empty values
            jersey_number = None
            if row.get('jersey_number'):
                try:
                    jersey_number = int(row['jersey_number'])
                except ValueError:
                    jersey_number = None
            
            # Convert weight to int, handling None/empty values
            weight = None
            if row.get('weight'):
                try:
                    weight = int(row['weight'])
                except ValueError:
                    weight = None
            
            # Create Bio instance
            bio = Bio(
                first_name=row.get('first_name'),
                last_name=row.get('last_name'),
                position=row.get('position') or None,
                jersey_number=jersey_number,
                weight=weight,
                height=row.get('height') or None,
                class_year=row.get('class_year') or None,
                hometown=row.get('hometown') or None,
                high_school=row.get('high_school') or None
            )
            
            bio_list.append(bio)
    
    return bio_list

