"""companies module"""

from modules import measurements
from modules.models.companies import Company

# consts
COMPANIESFILE = 'imports/companies.txt'

companies = []

def analyze():
    """Analyze unknown companies"""
    unknown_companies = []

    try:
        with open(COMPANIESFILE, mode='r') as rows:
            for row in rows:
                code = row[0:4].strip()
                name = row[5:24].strip()
                width_coord = row[87:89].strip()
                length_coord = row[90:92].strip()
                imported_company = Company(code, name, width_coord, length_coord)
                companies.append(imported_company)
            
            # Check if any company has the same coords
            for company in measurements.companies:
                is_known_company = False

                for known_company in companies:
                    if company[0] == known_company.get_width_coord() and company[1] == known_company.get_length_coord():
                        is_known_company = True
                        break
            
                # Otherwise it will added to the unknown companies list
                if is_known_company == False:
                    unknown_companies.append(Company("", "", company[0], company[1], company[2]))
                    
        print('Bestand', COMPANIESFILE, 'ingelezen')
        print('Onbekende bedrijven:')
        for unknown_company in unknown_companies:
            unknown_company.showUnknown()
    except FileNotFoundError:
        print('Bestand', COMPANIESFILE, 'niet gevonden')
