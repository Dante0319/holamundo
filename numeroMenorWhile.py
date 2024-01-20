numeros = [2,5,7,8,4,10,15,3,8]

i = 0
lowNum = numeros[0]
while i < len(numeros):
    if numeros[i] < lowNum:
        lowNum = numeros[i]
    i += 1

print('El numero menor es:', lowNum)
