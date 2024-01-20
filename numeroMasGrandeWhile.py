numeros = [5,7,8,4,10,15,3,8]

i = 0
bigNum = 0
while i < len(numeros):
    if numeros[i] > bigNum:
        bigNum = numeros[i]
    i += 1

print('El numero mayor es:', bigNum)
