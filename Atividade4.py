##ler 10 valores e escrever quantos desses valores lidos estao no intervalo[10,20](incluindo os valores 10 e 20 no
# intervalo) e quantos deles estão nao estão neste intervalo

cont=0
cont2=0

for x in range(1,11):
    n=int(input("digite um número: "))
    if n>=10 and n<=20:
        cont=cont+1
    else:
        cont2=cont2+1


print(cont)
print(cont2)