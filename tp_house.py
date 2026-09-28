import numpy as np

data = np.load("data/house/house.npz")
print(data)

surfaces = data["np_surfaces"]
loyers = data["np_loyers"]
print(loyers)

# Afficher les loyers & surfaces min & max
# Créer le tableau loyer_m2 = loyer par m²
# moyenne np.mean(loyer_m²) = loyer au m² moyen
# Afficher les surfaces > 200
# Afficher les loyers dont les surfaces > 200
# Afficher les loyers > loyer au m² moyen * surfaces
# Bonus : Ecart type = np.std, afficher les loyers > loyer moyen au m² * surfaces + 3 std