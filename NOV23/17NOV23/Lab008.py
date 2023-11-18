import csv

with open("Details.csv", newline="") as csv_obj:
    reader = csv.reader(csv_obj)
    for row in reader:
        print(row[0], row[1], row[2], sep="|")
