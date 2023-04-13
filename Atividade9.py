##faça um codigo para ler 2 valores e realize a divisão do primeiro pelo segundo valor recebido,
#caso o segundo valor digitado, seja zero, solicite novamente o valor, informando que so
#aceitaremos valores diferentes de zero

n1=float(input("digite um numero: "))
n2=float(input("digite outro numero: "))

while n2==0:
    print("digite um número diferente de zero")
    n2 = float(input("digite outro numero: "))
print("A divisao dois dois números é: ",n1/n2)