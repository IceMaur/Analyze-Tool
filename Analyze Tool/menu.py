# The start of the application. It show a menu with options

from modules import companies
from modules import inspectors
from modules import measurements
from modules import visitReports

if __name__ == "__main__":
    while True:
        print('Hoofdmenu')
        print('=========')
        print('1. Inlezen permanente gegevens')
        print('2. Inlezen metingen bestand')
        print('3. Analyseren meetgegevens')
        print('4. Toon inspecteurs')
        print('5. Importeer bezoekrapporten')
        print('6. Tonen bezoekrapporten per inspecteur')
        print('7. Tonen bezoekrapporten per bedrijf')
        print('0. stoppen\n')

        try:
            choice = int(input('Uw keuze : '))
        except ValueError:
            choice = -1

        if choice == 1:
            inspectors.import_inspectors()
        elif choice == 2:
            measurements.read_gasses()
        elif choice == 3:
            companies.analyze()
        elif choice == 4:
            inspectors.show_inspectors()
        elif choice == 5:
            inspectors.import_visit_reports()
        elif choice == 6:
            visitReports.show_visit_reports_by_inspector()
        elif choice == 7:
            visitReports.show_visit_reports_by_company()
        elif choice == 0:
            exit()
        else:
            print('ongeldige keuze')
        
        # New line after the chosen option.
        print()
