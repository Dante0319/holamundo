numeros = [5,7,8,4,10,15,3,8]

x = 0
multi = 1
while x < len(numeros):
    multi *= numeros[x]
    x += 1

print('La multiplicación es:', multi, '😎')