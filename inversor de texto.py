string = str(input('Insira uma string: '))

invertido = ""

for i in range(len(string) -1, -1, -1):
    invertido += string[i]

print('String invertida: ', invertido)