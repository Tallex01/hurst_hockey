import csv
from models import Stats


def create_stats_instances():
    """
    Read the bio.csv file and create a list of Bio instances.
    
    Returns:
        list: A list of Bio objects populated from the bio.csv file
    """
    stats_list = []
    
    with open('stats.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Convert jersey_number to int, handling None/empty values
            jersey_number = None
            if row.get('jersey_number'):
                try:
                    jersey_number = int(row['jersey_number'])
                except ValueError:
                    jersey_number = None
            
            # Create stats instance
            stats = Stats(
                jersey_number=jersey_number,
                first_name=row.get('first_name'),
                last_name=row.get('last_name'),
                GP =row.get('GP') or None,
                G = row.get('G') or None,
                A = row.get('A') or None,
                PTS = row.get('PTS') or None,
                SH = row.get('SH') or None,
                SH_PCT = row.get('SH_PCT') or None,
                Plus_Minus = row.get('Plus_Minus') or None,
                PPG = row.get('PPG') or None,
                SHG = row.get('SHG') or None,
                FG = row.get('FG') or None,
                GWG = row.get('GWG') or None,
                GTG = row.get('GTG') or None,
                OTG = row.get('OTG') or None,
                HTG = row.get('HTG') or None,
                UAG = row.get('UAG') or None,
                PN_PIM = row.get('PN_PIM') or None,
                MIN = row.get('MIN') or None,
                MAJ = row.get('MAJ') or None,
                OTH = row.get('OTH') or None,
                BLK = row.get('BLK') or None
            )
            
            stats_list.append(stats)
    
    return stats_list

