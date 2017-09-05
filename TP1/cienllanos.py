import scipy as sp
import matplotlib.pyplot as plt 
import sys
import math
import pylab as pl
import numpy as np

entrada = open(sys.argv[1])
etiquetas = list(entrada.readline().split())

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
datoGrafica = []
datoGrafica.append(tiempo_sol)
datoGrafica.append(tiempo_nublado)
datoGrafica.append(tiempo_lluvia)

if sys.argv[2]==1:
	X = np.arange(12)
	Y = np.arange(30)
	plt.bar(X + 0.00, datoGrafica[0], color = "b", width = 0.25, label = "Tiempo soleado")
	plt.bar(X + 0.25, datoGrafica[1], color = "g", width = 0.25, label = "Tiempo nublado")
	plt.bar(X + 0.50, datoGrafica[2], color = "r", width = 0.25, label = "Tiempo lluvioso")

	plt.xticks(X+0.38, ["1","2","3","4","5","6","7","8","9","10","11","12"])

	plt.ylabel('Tiempo en segundos')
	plt.xlabel('Atleta')
	plt.legend(loc = "upper right")

else:
	promedioTiempoSol = (reduce((lambda x ,y: x + y), tiempo_sol))/len(tiempo_sol)
	promedioTiempoNublado = (reduce((lambda x ,y: x + y), tiempo_nublado))/len(tiempo_nublado)
	promedioTiempoLLuvia = (reduce((lambda x ,y: x + y), tiempo_lluvia))/len(tiempo_lluvia)
	tiempos = ("Soleado","Nublado", "Lluvioso")
	tiempoPromedio = (promedioTiempoSol,promedioTiempoNublado,promedioTiempoLLuvia)
	position_x = np.arange(len(tiempos))
	X = np.arange(1)
	plt.bar(position_x[0]-0.25, promedioTiempoSol, color = "b", width = 0.50, label = (str)(promedioTiempoSol)+"seg")
	plt.bar(position_x[1]-0.25, promedioTiempoNublado, color = "g", width = 0.50, label = (str)(promedioTiempoNublado)+"seg")
	plt.bar(position_x[2]-0.25, promedioTiempoLLuvia, color = "r", width = 0.50, label = (str)(promedioTiempoLLuvia)+"seg")

	plt.xticks(position_x,tiempos)
	plt.ylabel('tiempos en segundos')
	plt.title("Promedios del tiempo")
	plt.legend(loc="upper left")
	
plt.show()


		
