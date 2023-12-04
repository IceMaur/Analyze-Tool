"""inspectors module"""

from modules.models.inspectors import Inspector
from modules.models.visitReports import VisitReport

# consts
INSPECTORFILE = 'imports/inspectors.txt'
VISITREPORTFILE = 'imports/visit reports.txt'

inspectors = []

def import_inspectors():
    """import the inspector file"""
    try:
        with open(INSPECTORFILE, mode='r') as rows:
            for row in rows:
                code = row[0:3]
                name = row[4:24]
                location = row[24:44]
                inspectors.append(Inspector(code, name, location))
        print('Bestand', INSPECTORFILE, 'ingelezen')
    except FileNotFoundError:
        print('Bestand', INSPECTORFILE, 'niet gevonden')

def show_inspectors():
    """An overview of all inspectors"""
    print("        Overzicht inspecteurs")
    print("        =====================\n")
    print("Code Naam                 Standplaats")
    print("---- -------------------- --------------------")
       
    for inspector in inspectors:
        inspector.show()

def import_visit_reports():
    """Add the visit reports to the the inspectors"""
    try:
        with open(VISITREPORTFILE, mode='r') as rows:
            for row in rows:
                inspector_code = row[0:3].strip()
                company_code = row[4:8].strip()
                visit_at = row[9:19].strip()
                created_at = row[20:30].strip()
                status = row[31:41].strip()
                comment = row[42:142].strip()

                for inspector in inspectors:
                    if inspector.get_code() == inspector_code:
                        inspector.add_visit_report(VisitReport(inspector_code, company_code, visit_at, created_at, status, comment))
                        break

        print('Bestand', VISITREPORTFILE, 'ingelezen')
    except FileNotFoundError:
        print('Bestand', VISITREPORTFILE, 'niet gevonden')
