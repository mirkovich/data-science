import scipy as sp
import matplotlib.pyplot as plt 
import sys
import math
import pylab as pl
import numpy as np
#~ x = sp.linspace(0,10,100)
#~ y = sp.sin(x)
#~ plt.figure()
#~ plt.plot(x,y)
#~ plt.show()

entrada = open(sys.argv[1])
etiquetas = list(entrada.readline().split())
#~ print etiquetas
datosBarras = []
tiempo_sol = []
tiempo_nublado = []
tiempo_lluvia = []
for line in entrada.readlines():
	datos = list(line.split())
	datos2= map(lambda x: (float)(x), datos)
	datoCorredor = datos2[1:4]
	datosBarras.append(datoCorredor) 
	tiempo_sol.append(datoCorredor[0])
	tiempo_nublado.append(datoCorredor[1])
	tiempo_lluvia.append(datoCorredor[2])
print tiempo_sol
datoGrafica = []
datoGrafica.append(tiempo_sol)
datoGrafica.append(tiempo_nublado)
datoGrafica.append(tiempo_lluvia)

X = np.arange(12)
plt.bar(X + 0.00, datoGrafica[0], color = "b", width = 0.25)
plt.bar(X + 0.25, datoGrafica[1], color = "g", width = 0.25)
plt.bar(X + 0.50, datoGrafica[2], color = "r", width = 0.25)



plt.xticks(X+0.38, ["1","2","3","4","5","6","7","8","9","10","11","12"])

plt.show()
