#!/usr/bin/python

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt	
import sys
import pylab as pl
import permutation_test as p

entrada = np.loadtxt(sys.argv[1],skiprows=1)

#~ conf es el parametro que nos dice que tipo de grafico realizar (hay dos opciones:)
#~ g grafica los datos sin ninguntratamiento previous
#~ p obtiene un promedio de los datos dadas las etiquetas 
conf = sys.argv[2]

#~ testing es  un bool que nos dice si hay que realizar un test o no 
testing = (3<len(sys.argv)) 
etiqueta = (5<len(sys.argv))
#~ recolectamos los tiempos segun cada etiqueta 
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
	count = count + 1 

#~ codigo para el grafico con el parametro g
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
	plt.show()
#~ codigo para el grafico con el parametro p
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
		plt.show()
	else:
		if conf == 't':
			if testing:
				#~ aca va el codigo dependiendo del testing que se quiere hacer  print sys.argv[3] es te tipo de testing
				testExecute = sys.argv[3]
				if etiqueta:
					inOne = sys.argv[4]
					inTwo = sys.argv[5]
					if inOne == "soleado":
						a = tiempo_soleado
					elif inOne == "nublado":
						a = tiempo_nublado
					elif inOne == "lluvioso":
						a = tiempo_lluvioso	

					if inTwo == "soleado":
						b = tiempo_soleado
					elif inTwo == "nublado":
						b = tiempo_nublado
					elif inTwo == "lluvioso":
						b = tiempo_lluvioso	
				#~ else:
					#~ print "Ingresar etiquetas: \n - soleado \n - nublado \n - lluvioso"
				#~ test de apareo
					if testExecute == "ttest":
						resultTest = stats.ttest_rel(a,b)
						print (resultTest)
					elif testExecute == "twil":
						resultTestRank = stats.wilcoxon(a,b)
						print (resultTestRank)
					elif testExecute == "tranksum":
						resultTestRankSum = stats.ranksums(a,b)	
						print (resultTestRankSum)
					elif testExecute == "tmann":
						resultTestMann = stats.mannwhitneyu(a,b)
						print (resultTestMann)
					elif testExecute == "tind":
						resultTestInd = stats.ttest_ind(a,b)
						print (resultTestInd)	
					elif testExecute == "tperm":
						#~ resultTestPerm =  
						print(p.permutationtest(a,b))
				else: 
					print ("Ingresar etiquetas: \n - soleado \n - nublado \n - lluvioso")		
			else: 
				print ("Ingrese el tipo de testing : \n - ttest: 	t-students de muestras apareadas \n - twil: 	test Wilconxon para muestras apareadas  \n - tranksum: 	test para muestras independientes   \n - tmann: 	test Mann-Whitney \n - tind: 	t-test de muestras independientes \n - tperm: 	test de permutacion")
	
		else:
			print ("Pasaje incorrecto de parametros, ingrese: \n - g si quiere graficar los datos, o \n - p si quiere el promedio total \n - t y a continuacion el tipo de testing: \n  # ttest \n  # twil \n  # tranksum \n  # tmann \n  # tind \n  # tperm")


	
		
