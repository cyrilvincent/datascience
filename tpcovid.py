import csv

with open("data/covid/covid-france.txt") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["NbCas"]) != 0:
            print(int(row["DC"]) / int(row["NbCas"]))

# Créer 3 listes : ixs, nbcas, dcs
# Caster les listes en np.array
# nbcas max, dc max
# Filtrer nbcas, ixs et dcs pour nbcas > 10
# Sur ces filtres créer le np.array letality et l'afficher
# Afficher la letalité min, max
