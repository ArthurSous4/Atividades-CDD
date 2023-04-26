listasnum = []
resp = "sim"
while resp=="sim":

    num1=int(input("digite um número: "))

    if num1 == 0:
        print("digite um numero diferente de 0")

    elif num1 < 0:
        print("este número é negativo")
        listasnum.append(num1)

    else:
        print("este número é positivo")
        listasnum.append(num1)

    print(f"numeros armazenados: {listasnum}")
    resp=(str(input("deseja digitar outro número?\n")))