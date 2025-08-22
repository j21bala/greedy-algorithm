distancia = int(input("Ingresa la distancia del punto A al B: "))
medida = [1,2,3,4,5]
pasos = []
numero_max = len(medida) - 1

while distancia > 0: 
    elefante = distancia - medida[numero_max]
    
    if elefante >= 0:
        distancia = elefante
        pasos.append(medida[numero_max])
    else:
        numero_max = numero_max - 1   

print(pasos)