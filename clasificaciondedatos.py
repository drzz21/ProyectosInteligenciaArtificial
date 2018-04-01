# instalamos los paquetes necesarios para el proyecto


#    pip install scipy
#    pip install numpy
#    python -mpip install -U matplotlib
#    python -mpip install -U sklearn

# además de esto se importaron las siguientes librerias usando los siguientes comandos

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np


# obtenemos los datos que necesitamos
# En la version aqui mostrada de la bd iris, las primeras dos columnas
# son medidas del sepalo y las otras dos son del petalo, no como en
# la que usa Iran Roman

iris = datasets.load_iris()
especies = iris.target_names
caracteristicas = iris.data


# creamos una figura
plt.figure(1)
# graficamos la longitud de petalo para el primer tipo de flores
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,2])
# agregamos la longitud de pétalo para el segundo tipo de flores
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,2])
# agregamos la longitud de pétalo para el tercer tipo de flores
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,2])
plt.ylabel('Longitud de Pétalo (cm)')
# mostramos la grafica
plt.show()

# creamos otra figura
plt.figure(2)
# graficamos la anchura del pétalo para el primer tipo de flores
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,3])
# agregamos la anchura del pétalo para el segundo tipo de flores
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,3])
# agregamos la anchura del pétalo para el tercer tipo de flores
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,3])
plt.ylabel('Anchura de Pétalo (cm)')
# mostramos la grafica
plt.show()

# creamos otra figura
plt.figure(3)
# graficamos la longitud del sépalo
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,0])
# agregamos la longitud del sépalo para el segundo tipo de flores
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,0])
# agregamos la longitud del sépalo para el tercer tipo de flores
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,0])
plt.ylabel('Longitud de Sépalo (cm)')
# mostramos la grafica
plt.show()

# creamos otra figura
plt.figure(4)
# graficamos la anchura del sépalo
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,1])
# agregamos la anchura del sépalo para el segundo tipo de flores
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,1])
# agregamos la anchura del sépalo para el tercer tipo de flores
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,1])
plt.ylabel('Anchura de Sépalo (cm)')
# mostramos la grafica
plt.show()


# Al parecer, las dos caracteristicas que mejor separan los tres tipos de flores fueron
# La longitud de Petalo y la Anchura de Pétalo. La siguiente figura muestra como estas dos caracteriticas
# diferencian los tres tipos de flores.
plt.figure(5)
plt.scatter(caracteristicas[0:49,2],caracteristicas[0:49,3])
plt.scatter(caracteristicas[50:99,2],caracteristicas[50:99,3])
plt.scatter(caracteristicas[100:149,2],caracteristicas[100:149,3])
plt.xlabel('Longitud de Pétalo (cm)')
plt.ylabel('Anchura de Pétalo (cm)')
plt.show()

# Experimenta generando otras figuras donde grafiquesotras caracteristicas en los ejesx,y.
# Determina si alguna otra pareja de caracteristicas sirve para diferenciar las tres especies de flores

# Para esta figura se compararán las caracteristicas de longitud de sépalo y anchura de sépalo
# se crea otra figura
plt.figure(6)
# se agregan las caracteristicas de largo y ancho del sepalo del primer tipo de flores
plt.scatter(caracteristicas[0:49,0],caracteristicas[0:49,1])
# se agregan las caracteristicas de largo y ancho del sepalo del segundo tipo de flores
plt.scatter(caracteristicas[50:99,0],caracteristicas[50:99,1])
# se agregan las caracteristicas de largo y ancho del sepalo del tercer tipo de flores
plt.scatter(caracteristicas[100:149,0],caracteristicas[100:149,1])
plt.xlabel('Longitud de Sépalo (cm)')
plt.ylabel('Anchura de Sépalo (cm)')
# se muestra la figura
plt.show()

# Para esta figura se compararán las caracteristicas de longitud de pétalo y longitud de sépalo
# se crea otra figura
plt.figure(7)
# se agregan las caracteristicas de largo de petalo y sepalo del primer tipo de flores
plt.scatter(caracteristicas[0:49,2],caracteristicas[0:49,0])
# se agregan las caracteristicas de largo de petalo y sepalo del segundo tipo de flores
plt.scatter(caracteristicas[50:99,2],caracteristicas[50:99,0])
# se agregan las caracteristicas de largo de petalo y sepalo del tercer tipo de flores
plt.scatter(caracteristicas[100:149,2],caracteristicas[100:149,0])
plt.xlabel('Longitud de Pétalo (cm)')
plt.ylabel('Longitud de Sépalo (cm)')
# se muestra la figura
plt.show()

# Para esta figura se compararán las caracteristicas de anchura de sépalo y anchura de pétalo
# se crea otra figura
plt.figure(8)
# se agregan las caracteristicas del ancho del petalo y del sepalo del primer tipo de flores
plt.scatter(caracteristicas[0:49,3],caracteristicas[0:49,1])
# se agregan las caracteristicas del ancho del petalo y del sepalo del segundo tipo de flores
plt.scatter(caracteristicas[50:99,3],caracteristicas[50:99,1])
# se agregan las caracteristicas del ancho del petalo y del sepalo del tercer tipo de flores
plt.scatter(caracteristicas[100:149,3],caracteristicas[100:149,1])
plt.xlabel('Anchura de Pétalo (cm)')
plt.ylabel('Anchura de Sépalo (cm)')
# se muestra la figura
plt.show()

