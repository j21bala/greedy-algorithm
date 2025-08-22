cantidad = int(input("Ingrese la n cantidad de números perfectos que desea: "))
lista_perfectos = []
num = 1


while len(lista_perfectos) < cantidad:
    
    suma_divisores = 0
    if num > 1:
        for i in range(1, num):
            if num % i == 0:
                suma_divisores += i
    if suma_divisores == num:
        lista_perfectos.append(num)
    num += 1

print("Los primeros", cantidad, "números perfectos son:", lista_perfectos)


