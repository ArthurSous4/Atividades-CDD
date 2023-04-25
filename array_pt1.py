'''
Altere o sistema anterior e faça um sistema de login, pedido a senha do usuario e mostrando seu nome e a mensagem, login
efetuado com sucesso
'''

senha=[]
nome=[]
for x in range(5):
    nome.append(str(input("digite seu nome")))
    senha.append(int(input("digite sua senha: ")))

for i in range(5):
    print(i, nome[i], senha[i])
