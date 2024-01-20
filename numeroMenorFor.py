numeros = [2,7,8,4,10,15,3,8]

lowNum = numeros[0]
for num in numeros:
    if num < lowNum:
        lowNum = num

print('El numero menor es:', lowNum)