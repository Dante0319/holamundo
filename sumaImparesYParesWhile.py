numeros = [5,7,8,4,10,15,3,8]

i = 0
impares = 0
pares = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        pares += numeros[i]
    else:
        impares += numeros[i]
    i += 1

print('La suma de los pares es:', pares)
print('El suma de los impares es:', impares)