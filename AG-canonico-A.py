import math
import random

def detNumero():

    nRandom=round(random.random(),1)
    if nRandom<0.5:
        return 0
    else:
        return 1

# Definicion de la funcion objetivo
def funcionObjetivo(x):

    return (x/(2**30)-1)**2

# funcion para generar la poblacion inicial
def generarPoblacion(numeroIndividuos, tamano):#Tamaño de la cadena binaria
    poblacion = []

    for i in range(numeroIndividuos):
        individuo=[]
        for j in range(tamano):
            individuo.append(detNumero())
        poblacion.append(individuo)
    
    return poblacion


# pasaje de un binario a decimal
def decimal(binario):
    decimal=0
    puntero=0
    for i in range (0,29):
        decimal = decimal + binario[puntero]*(2**(29-puntero))
        puntero+=1
        if puntero==29:
            decimal+=1
    return decimal



# Funcion fitness
def fitnes(poblacion, numeroIndividuos):
    acum = 0
    fitness = []
    
    indice = 0
    while indice < numeroIndividuos:
        x = decimal(poblacion[indice])
        acum += funcionObjetivo(x)
        indice += 1

    indice = 0
    while indice < numeroIndividuos:
        x = decimal(poblacion[indice])
        fit = funcionObjetivo(x) / acum 
        fitness.append(fit)
        indice += 1

    return fitness


poblacion=generarPoblacion(numeroIndividuos=10,tamano=30)
acum=0
fit=fitnes(poblacion,10)
print("               arreglo binario                                                              decimal       funcion           fitnes")
for i in range (0,9):
    deci=decimal(poblacion[i])
    print (poblacion[i], deci ,funcionObjetivo(deci),fit[i])
