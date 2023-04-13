##Ler 10 valores e escrever quantos desses valores lidos são negativos
cont=0
for x in range(1,11):
    n=int(input("digite um número:"))
    if n<0:
         cont=cont+1
print("foram encontrados",cont,"numeros negativos")