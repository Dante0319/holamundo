message = "Estamos programando en Python"
vowels = "aeiou"
words = message.split()

print(len(message))
print(message.lower())
print(message.upper())
print(words)

cont = 0
for i in message:
    if i.lower() in vowels:
        cont += 1
print("hay", cont, 'vocales')
