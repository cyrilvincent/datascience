# Créer un tableau a1 = -2pi à +2pi avec un pas de 0.01
# Créer le tableau asin qui applique un sin sur a1
# Créer le tableau acos qui applique le cos sur a1
# acos² + asin1 vérifier que vous obtenez que des 1
# Afficher la size du tableau et prendre les valeurs sur asin de 0 à 2pi et prendre une valeur sur 10 [size//2::2]

import numpy as np

a1 = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
asin = np.sin(a1)
acos = np.cos(a1)
print(np.round(asin ** 2 + acos ** 2, 2))
print(a1.size)
print(asin[a1.size // 2::10])