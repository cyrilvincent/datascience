import csv

with open("data/covid/covid-france.txt") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["NbCas"]) != 0:
            print(int(row["DC"]) / int(row["NbCas"]))