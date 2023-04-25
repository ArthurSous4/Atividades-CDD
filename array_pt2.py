passw=[]
nome=[]

for x in range(5):
    nome.append(str(input("digite seu nome: ")))
    passw.append(int(input("digite sua senha: ")))

usuario= input("digite o ususario para login: ")
senha= input("digite a senha para login: ")

for y in range(5):
    if usuario==nome[y] and senha==passw:
        print("login efetuado com sucesso")
        break ##encerra a busca por outro usuario cadastrado




