#!/usr/bin/python
# -*- coding: utf-8 -*-

print(__doc__)

# Cargamos las librerias utilizadas

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

# Importamos los datos que vamos a manipular de la bd iris
iris = datasets.load_iris()
X = iris.data[:, :2]  # Solo tomamos los primeros dos datos de iris
y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Graficamos los puntos deseados usando scatter
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.xlabel('Largo del sepalo')
plt.ylabel('Ancho del sepalo')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

# Hacemos un analisis de los componentes principales usando PCA de Python
# esto sirve para descomponer los valores singulares de los datos para proyectarlos a un espacio dimensional inferior.
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

# Mostramos la imagen de la grafica obtenida
plt.show()
