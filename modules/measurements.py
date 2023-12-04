"""Measurements module"""

import numpy             as np
import matplotlib.pyplot as plt
import csv

# consts
GASSESFILE = 'imports/gasses.csv'
GASSESCALCULATEDFILE = 'imports/gasses calculated.csv'
C1 = 1
C2 = 25
C3 = 5
C4 = 1000

companies = []

def read_gasses():
    """Read CO2 data from the csv-gasses file"""

    gas_calculated_rows = []

    try:
        with open(GASSESFILE, newline='') as csvfile:
            gas_rows = list(csv.reader(csvfile))
            gas_rows.pop(0)
            with open(GASSESCALCULATEDFILE, 'w', newline='') as calculatedfile:
                csvwriter = csv.writer(calculatedfile)
                csvwriter.writerow(["breedtegraad", "lengtegraad", "Totale uitstoot"])
                for gas_row in gas_rows:
                    gas_calculated_rows.append([gas_row[0], gas_row[1], float(gas_row[2]) * C1 + float(gas_row[3]) * C2 + float(gas_row[4]) * C3 + float(gas_row[5]) * C4])

                csvwriter.writerows(gas_calculated_rows)

        gas_array = (np.loadtxt(GASSESCALCULATEDFILE, delimiter=',', skiprows=1, usecols=2)).reshape((100,100))
    except FileNotFoundError:
        print('Bestand', GASSESFILE, 'niet gevonden')
        return
    except IndexError:
        print("Het bestand heeft een rij met niet het juiste aantal kolommen")
        return
    except ValueError:
        print('Bestand heeft een ongeldige waarde')
        return
    
    gas_value_current_row = 0
    same_value_in_a_row = 1
    skip_coords = []
    for gas_calculated_row in gas_calculated_rows:
        # if it has 5 times the same value, add the coords and calculation to the companies list
        if (same_value_in_a_row == 5 and [gas_calculated_row[0], gas_calculated_row[1]] not in skip_coords):
            companies.append([str(int(gas_calculated_row[0]) + 2), str(int(gas_calculated_row[1]) - 3), gas_calculated_row[2] * 16 + gas_calculated_row[2] * 2 * 8 + gas_calculated_row[2] * 4])
            skip_coords.append([str(int(gas_calculated_row[0]) + 4), gas_calculated_row[1]])
            same_value_in_a_row = 1
        elif gas_value_current_row == gas_calculated_row[2]:
            same_value_in_a_row += 1
        else: 
            gas_value_current_row = gas_calculated_row[2]
            same_value_in_a_row = 1

    print('Bestand', GASSESFILE, 'ingelezen')
    print()
    print("Gasses")
    print(gas_array)
    print("Comapnies")
    print(companies)
    plt.imshow(gas_array)
    plt.colorbar()
    plt.show()
