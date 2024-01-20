numeros = [5,7,8,4,10,15,3,8]

contImpares = 0
contPares = 0
impares = 0
pares = 0
for num in numeros:
    if num % 2 == 0:
        pares += num
        contPares += 1
    else:
        impares += num
        contImpares += 1

print('Total pares:', contPares, '\nTotal impares:', contImpares)
print('Suma pares:', pares, '\nSuma impares:', impares)