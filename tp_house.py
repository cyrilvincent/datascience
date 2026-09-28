import numpy as np
import matplotlib.pyplot as plt

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

print(np.min(loyers), loyers.max())
loyer_m2 = loyers / surfaces
print(loyer_m2)
loyer_m2_mean = np.mean(loyer_m2)
print(loyer_m2_mean)
filter = surfaces > 200
print(surfaces[filter])
print(loyers[filter])
print(loyers[loyers > loyer_m2_mean * surfaces])
loyer_m2_std = np.std(loyer_m2)
print(loyer_m2_std)
print(loyers[loyers > loyer_m2_mean * surfaces + 3 * loyer_m2_std * surfaces])

plt.subplot(2,2,1)
plt.scatter(surfaces, loyers)
x = np.arange(400)
y = x * loyer_m2_mean
plt.plot(x, y, color="red")
plt.subplot(2,2,2)
plt.bar(np.arange(20), np.histogram(surfaces, bins=20)[0])
plt.subplot(2,2,3)
plt.hist(loyers, bins=20)
plt.subplot(2,2,4)
plt.hist(loyer_m2, bins=20)
plt.show()
# Afficher le nuage de point surface vs loyer
# bonus : rendre jolie
# Afficher l'histogram np.histogram(surfaces, bins=10) des surfaces, loyers et loyer_m2
# Mettre tout celà dans un subplot 2x2
# Grâce au loyer_m2_mean afficher un plot x = np.arange(400) y = x * loyer_m2_mean
# Bonus faire la même chose pour 1 std, 2 std, 3 std




