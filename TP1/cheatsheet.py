import numpy as np
from scipy import stats
import matplotlib.pyplot as plt	
import sys
import pylab as pl

entrada = np.loadtxt(sys.argv[1],skiprows=1)
conf = sys.argv[2]
tiempo_soleado = []
tiempo_nublado = []
tiempo_lluvioso = []
atletas = []
count = 1
for line in entrada:
	tiempo_soleado.append(line[1])
	tiempo_nublado.append(line[2])
	tiempo_lluvioso.append(line[3])
	atletas.append((str)(count))
	count = count +1 

if conf == 'g':
	X = np.arange(len(tiempo_soleado))
	Y = np.arange(30)
	plt.bar(X + 0.00, tiempo_soleado, color = "b", width = 0.25, label = "Tiempo soleado")
	plt.bar(X + 0.25, tiempo_nublado, color = "g", width = 0.25, label = "Tiempo nublado")
	plt.bar(X + 0.50, tiempo_lluvioso, color = "r", width = 0.25, label = "Tiempo lluvioso")

	plt.xticks(X + 0.38, atletas)

	plt.ylabel('Tiempo en segundos')
	plt.xlabel('Atleta')
	plt.legend(loc= "upper right")

else:
	if conf == 'p':
		promedioTiempoSol = (reduce((lambda x ,y: x + y), tiempo_soleado))/len(tiempo_soleado)
		promedioTiempoNublado = (reduce((lambda x ,y: x + y), tiempo_nublado))/len(tiempo_nublado)
		promedioTiempoLLuvia = (reduce((lambda x ,y: x + y), tiempo_lluvioso))/len(tiempo_lluvioso)
		tiempos = ("Soleado","Nublado", "Lluvioso")
		position_x = np.arange(len(tiempos))
		X = np.arange(1)
		plt.bar(position_x[0]-0.25, promedioTiempoSol, color = "b", width = 0.50, label = (str)(promedioTiempoSol)+"seg")
		plt.bar(position_x[1]-0.25, promedioTiempoNublado, color = "g", width = 0.50, label = (str)(promedioTiempoNublado)+"seg")
		plt.bar(position_x[2]-0.25, promedioTiempoLLuvia, color = "r", width = 0.50, label = (str)(promedioTiempoLLuvia)+"seg")

		plt.xticks(position_x,tiempos)
		plt.ylabel('tiempos en segundos')
		plt.title("Promedios del tiempo")
		plt.legend(loc="upper left")
	else:
		print "pasaje incorrecto de parametros, ingrese \n g si quiere graficar los datos, o \n p si quiere el promedio total"

plt.show()	
		
