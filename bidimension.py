import pandas as pd

datos = pd.DataFrame(["carlos", "yuca", "frijol", "alverja"], columns=['val1'])

correo = "@banano.com.co"

val2 = []

for i in datos['val1']:
    val2.append(i + correo)

datos['val2'] = val2
print(datos)