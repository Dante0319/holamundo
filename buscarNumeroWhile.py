numeros = [5,7,8,4,10,15,3,8]
num = int(input("Ingrese un numero para buscar: "))
isInList = False 
x = 0
suma = 0
while x < len(numeros):
    if num == numeros[x]:
        isInList = True
    x += 1

if isInList:
    print('El numero:', num, 'si esta 😁')
else:
    print('El numero:', num, 'no esta 😢')