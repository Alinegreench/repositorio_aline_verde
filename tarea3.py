#Crear un programa que genere 100 numeros aleatorios entre 1 y 1000
#inserte en un alista los pares y en otr alos impares
#Imprimir ambas listas y el tamaño de las mismas

import random

numeros= [random.randint(1, 1001) for i in range(100)]

lambda_esPar = lambda x: True if x%2 == 0 else False

pares = []
for x in numeros:
    if lambda_esPar(x) == True:
        pares.append(x)

impares =[]
for x in numeros:
    if lambda_esPar(x) == False:
        impares.append(x)

print(f"La lista generada es: {numeros}")
print(f"Pares: {pares}")     
print(f"Impares: {impares}")       
print("El tamaño de la lista de pares es:", len(pares))
print("El tamaño de la lista de impares es:", len(impares))