##ler um valor N e imprimir todos os valores inteiros entre 1(inclusive) e N(inclusive).
# Considere que o N sera sempre maior que zero
n=int(input("digite um numero: "))
for x in range(0,n+1):
    if n<1:
        print("digite um número valido")
    else:
        print(x)