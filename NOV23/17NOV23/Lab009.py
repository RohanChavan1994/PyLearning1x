import csv

data = [
    ["Bobby", 26, "KA"],
    ["Damian", 32, "US"],
    ["Carlos", 21, "PR"]
]

with open("Details.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)
