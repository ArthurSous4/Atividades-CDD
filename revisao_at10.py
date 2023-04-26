invalido="sim"
eleitores=int(input("quantos eleitores existem: "))
while invalido=="sim":

    votobranco=int(input("quantos votos brancos existem: "))
    votonulo=int(input("quantos votos nulos existem: "))
    votovalido=int(input("quantos votos validos existem: "))

    votosTotais=votonulo+votobranco+votovalido

    if votosTotais>eleitores or votosTotais!=eleitores:
        print("o numeros de votos excedeu ou não alcancou o número de eleitores ")
    else:
        invalido="nao"

print(f"votos brancos: {(votobranco)*eleitores/100}%\nvotos nulos: {(votonulo)*eleitores/100}%\nvotos validos: {(votovalido)*eleitores/100}%")



