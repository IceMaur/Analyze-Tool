from datetime import date
from modules.companies import companies
from modules.inspectors import inspectors

def show_visit_reports_by_inspector():
    """Get the visit reports by the inspector code and optional a start and an end date"""
    
    # Create a new list, so that we didn't remvove reports from the inspector by the filter
    visit_reports =  list(__get_visit_reports_by_inspector_code_input())
    __visit_reports_filter_dates(visit_reports)

    # Show visit reports
    visit_reports.sort(key=__get_visit_at, reverse=True)
    print()
    print("Bezoekrapporten:")
    print("naam bedrijf, bezoekdatum, datum van het rapport, opmerking, status")
    print("-------------------------------------------------------------------")
    for visit_report in visit_reports:
        for company in companies:
            if company.get_code() == visit_report.get_company_code():
                print(company.get_name() + ', ' + str(visit_report.get_visit_at()) + ', ' + str(visit_report.get_created_at()) + ', ' + visit_report.get_comment() + ', ' + visit_report.get_status())

def show_visit_reports_by_company():
    """Get the visit reports by the company code and optional a start and an end date"""
    
    # Create a new list, so that we didn't remvove reports from the inspector by the filter
    visit_reports = list(__get_visit_reports_by_company_code_input())
    __visit_reports_filter_dates(visit_reports)

    # Show visit reports
    visit_reports.sort(key=__get_visit_at, reverse=True)
    print()
    print("Bezoekrapporten:")
    print("naam inspecteur     bezoekdatum, datum van het rapport, opmerking, status")
    print("-------------------------------------------------------------------------")
    for visit_report in visit_reports:
        for inspector in inspectors:
            if inspector.get_code() == visit_report.get_inspector_code():
                print(inspector.get_name() + str(visit_report.get_visit_at()) + ', ' + str(visit_report.get_created_at()) + ', ' + visit_report.get_comment() + ', ' + visit_report.get_status())

#
# Private Functions
#

def __get_visit_at(report):
    return report.get_visit_at()

def __code_input(name_field):
    """Show code input and get the filled in code"""
    try:
        return input(name_field + ' : ')
    except ValueError:
        print('Geen geldige code')
        return __code_input(name_field)
    
def __visit_date_input(name_field):
    """Show the visit date input and get the filled visit date"""
    try:
        dateInput = input(name_field + ' bezoekdatum dd-mm-yyyy (optioneel) : ')
        if not dateInput.strip():
            return None
        return date(int(dateInput[6:10]), int(dateInput[3:5]), int(dateInput[0:2]))
    except:
        print('Ongeldige datum')
        return __visit_date_input(name_field)
        
def __get_visit_reports_by_inspector_code_input():
    """Get all the visit reports of the inspector by the inspector code from the input"""
    inspector_code = __code_input('Inpecteur code')

    for inspector in inspectors:
        if inspector.get_code() == inspector_code:
            return inspector.get_visit_reports()
        
    print('Geen bestaande inspecteur voor deze code')
    return __get_visit_reports_by_inspector_code_input()
        
def __get_visit_reports_by_company_code_input():
    """Get all the visit reports of the company by the company code from the input"""
    company_code = __code_input('Bedrijfscode')

    visit_reports = []
    for inspector in inspectors:
        for visit_report in inspector.get_visit_reports():
            if visit_report.get_company_code() == company_code:
                visit_reports.append(visit_report)
    
    if visit_reports:
        return visit_reports

    print('Geen bestaande bedrijf voor deze code')
    return __get_visit_reports_by_company_code_input()

def __visit_reports_filter_dates(visit_reports):
    """Start and end visit date filter for visit reports"""
    start_date = __visit_date_input('Start')
    end_date = __visit_date_input('Eind')

    # Start and end visit date filter
    __visit_reports_filter_by_dates(visit_reports, start_date, end_date)

def __visit_reports_filter_by_dates(visit_reports, start_date, end_date):
    """Filter visit reports by start and end visit date"""
    if start_date or end_date:
        for visit_report in visit_reports:
            visit_report_at = visit_report.get_visit_at()
            if (start_date and start_date > visit_report_at) or (end_date and end_date < visit_report_at):
                visit_reports.remove(visit_report)
