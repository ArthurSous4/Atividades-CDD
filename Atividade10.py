senha="1234"
contadorban=1
senhausuario=str(input("Digite sua senha: "))

if senhausuario!=senha:
    while senhausuario!=senha and contadorban!=3:

        print("SENHA INCORRETA\n Tente novamente")
        contban=contadorban+1
        senhausuario = str(input("Digite sua senha: "))

        if contadorban==3:
            print("\033[1;31mVoce foi BANIDO\033[m")
        else:
            print("BEM VINDO usuário")
else:
    print("BEM VINDO usuário")






