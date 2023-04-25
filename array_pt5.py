'''
Escreva um algoritmo  que solicite ao usuario a entrada de 5 nomes, e que exiba a lista desses nomes na tela.
apos exibir essa lista, o programa deve  mostrar também os nomes na ordem inversa que o usuario digitou, um
por linha
'''

lista=[]

for x in range(5):
    lista.append(str(input("digite um nome")))

for y in range(-1,-6,-1):
    print(lista[y])