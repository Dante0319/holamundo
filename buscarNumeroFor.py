numeros = [5,7,8,4,10,15,3,8]
num = int(input("Ingrese un numero para buscar: "))
isInList = False 
x = 0
for x in numeros:
    if num == x:
        isInList = True

if isInList:
    print('El numero:', num, 'si esta 😁')
else:
    print('El numero:', num, 'no esta 😢')