#pip install Pillow
from PIL import Image
import numpy as np

print(Image.__version__)
im = Image.open("data/img/ski.jpg") #RGB
cube = np.asarray(im)
print(cube.shape)
red = cube[:,:,0]
print(np.min(red), np.max(red), np.mean(red), np.std(red))
red_modified = red - 20
red_modified = np.clip(255,0,red_modified)

im = Image.fromarray(red_modified).convert("RGB")
im.save("data/img/modified.jpg")

# TP
# Charger l'image avec Pillow et afficher son shape
# Prende un canal de couleur et afficher sa luminosité moyenne + contraste
# Normaliser l'image pixel - abs(luminosite - 127.5)
# Sauvegarder l'image
# Créer une N&B
# Correction à 10h40

