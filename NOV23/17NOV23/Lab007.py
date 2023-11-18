import csv

with open("Details.csv", newline="") as csv_obj:
    reader = csv.reader(csv_obj)
    for row in reader:
        print('|'.join(row))
