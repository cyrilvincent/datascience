import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.stats as stats

# Charger data/house/house.csv et créer les vecteurs surfaces, loyers
# Afficher le nuage de points surface / loyer
# min, max, avg, std, media, quartile sur loyer et surface
# loyerperm2 = loyer / surface
# min, max, avg, std, media, quartile sur loyerperm2
# Normal?
# Filtrer les points en fonction de ce que vous déciderez
# min, max, avg, std, media, quartile sur loyerperm2 filtré

surfaces = []
loyers = []
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        surfaces.append(float(row["surface"]))
        loyers.append(float(row["loyer"]))
surfaces = np.array(surfaces)
loyers = np.array(loyers)

print(f"Loyer min:{np.min(loyers)}, max:{np.max(loyers)}, avg:{np.mean(loyers)}, std:{np.std(loyers)}, median:{np.median(loyers)}, quartiles:{np.quantile(loyers, [0.25,0.75])}")
print(f"Surface min:{np.min(surfaces)}, max:{np.max(surfaces)}, avg:{np.mean(surfaces)}, std:{np.std(surfaces)}, median:{np.median(surfaces)}, quartiles:{np.quantile(surfaces, [0.25,0.75])}")
plt.scatter(surfaces, loyers)
plt.show()

loyersperm2 = loyers / surfaces
print(f"Loyerperm2 min:{np.min(loyersperm2)}, max:{np.max(loyersperm2)}, avg:{np.mean(loyersperm2)}, std:{np.std(loyersperm2)}, median:{np.median(loyersperm2)}, quartiles:{np.quantile(loyersperm2, [0.25,0.75])}")
plt.scatter(np.arange(len(loyersperm2)), loyersperm2)
plt.show()
loyersperm2_filter = loyersperm2[surfaces < 200]
loyersperm2_filter = loyersperm2_filter[loyersperm2_filter < 38 + 3 * 10]
print(f"Loyerperm2_filter min:{np.min(loyersperm2_filter)}, max:{np.max(loyersperm2_filter)}, avg:{np.mean(loyersperm2_filter)}, std:{np.std(loyersperm2_filter)}, median:{np.median(loyersperm2_filter)}, quartiles:{np.quantile(loyersperm2_filter, [0.25,0.75])}")
plt.scatter(np.arange(len(loyersperm2_filter)), loyersperm2_filter)
plt.show()

