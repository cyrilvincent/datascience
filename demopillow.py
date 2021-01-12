#pip install Pillow
from PIL import Image
import numpy as np

print(Image.__version__)
im = Image.open("data/img/ski.jpg") #RGB
cube = np.asarray(im)
print(cube.shape)
red = cube[:,:,0]
print(np.min(red), np.max(red), np.mean(red), np.std(red))
nb = cube.mean(axis=2)
print(np.min(nb), np.max(nb), np.mean(nb), np.std(nb))
delta = np.mean(nb) - 127.5
delta_std = np.abs(np.std(nb) - 63.75)
nb = (nb - delta) * 63.75 / delta_std
nb = np.clip(nb, 0, 255)
im = Image.fromarray(nb).convert("RGB")
im.save("data/img/modified.jpg")

# TP
# Charger l'image avec Pillow et afficher son shape
# Prende un canal de couleur et afficher sa luminosité moyenne + contraste
# Normaliser l'image pixel - abs(luminosite - 127.5)
# Sauvegarder l'image
# Créer une N&B
# Correction à 10h40

