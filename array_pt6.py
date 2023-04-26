lista=[]
somatotal=0
media=0
contadorMedia=0
for x in range(5):
    numero = int(input("digite um numero: "))
    lista.append(numero)
    somatotal += numero
media=somatotal/5
print(f"{lista} - {somatotal} - {media}")
##1
for x in range(5):
    if lista[x]%2==0:
        print(lista[x])
##2
maiorNumero=lista[0]
menorNumero=lista[0]
for y in range(5):
    if maiorNumero < lista[y]:
        maiorNumero = lista[y]
print(maiorNumero)

for z in range(5):
    if menorNumero > lista[z]:
        menorNumero = lista[z]

print(menorNumero)
##3
for i in range(5):
    if media < lista[i]:
        contadorMedia=contadorMedia+1

print(contadorMedia)
