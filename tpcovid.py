import csv
import numpy as np

ixs = []
nbcas = []
dcs = []

with open("data/covid/covid-france.txt") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ixs.append(int(row["ix"]))
        nbcas.append(int(row["NbCas"]))
        dcs.append(int(row["DC"]))

ixs = np.array(ixs)
nbcas = np.array(nbcas)
dcs = np.array(dcs)

print(nbcas)
print(dcs)

print(f"NbCas: {np.max(nbcas)}")
print(f"DC: {np.max(dcs)}")

nbcas_filter = nbcas[nbcas > 10]
ixs_filter = ixs[nbcas > 10]
dcs_filter = dcs[nbcas > 10]
print(f"Shape: {nbcas_filter.shape}")
if dcs_filter.shape == nbcas_filter.shape:
    letality = dcs_filter / nbcas_filter
print(letality)
print(f"Letality min: {np.min(letality)}, max: {np.max(letality)}")

# Afficher les nbcas et dcs en superposition
# Afficher la letalite dans un subplot en dessous
# Sauvegarder letality dans un npz dans data
# Recharger le npz
