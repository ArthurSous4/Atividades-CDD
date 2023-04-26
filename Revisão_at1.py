listaNotas = []
resposta = "sim"
while resposta == "sim":
    num1=float(input("digite um numero: "))
    num2=float(input("digite outro número: "))

    media = (num1+num2)/2

    listaNotas.append(media)

    print(f"sua media é {media}")

    if media < 4 :
        print("voce foi reprovado")

    elif media >= 4 and media < 7:
        print("voce esta em recuperação")

    else:
        print("voce foi aprovado")

    print("medias cadastradas: ",listaNotas)
    resposta=str(input("quer tentar novamente?('sim' ou 'não')\n"))






