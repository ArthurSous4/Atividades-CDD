'''
Faça um codigo para ler um vetor de 30 numeros. apos isto, ler mais um numero qualquer, calcular e escrever quantas
vezes esse Número aparece no vetor.
'''

lista=[]
contadoriguais=0

for x in range(10):
    lista.append(int(input("Digite um numero: ")))

num=int(input("digite o número que que achar:"))

for y in range(10):
    if num==lista[y]:
        contadoriguais=contadoriguais+1

print(f"o número '{num}' existe {contadoriguais} vezes")

