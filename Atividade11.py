'''
Escreva um codigo para ler as notas dos alunos da 1a. e 2a. avaliacoes de um aluno, calcule e
imprima a media desse aluno. so devem ser aceitos valores validos, durante a leitura, (0 a 10)
para cada nota
'''
resposta="sim"
while resposta=="sim":

    nota1=float(input("digite a sua nota da 1* avaliação: "))

    while nota1<0 or nota1>10:
        print("nota inválida")
        nota1 = float(input("digite a sua nota da 1* avaliação: "))

    nota2=float(input("digite a sua nota da 2* avaliação: "))

    while nota2<0 or nota2>10:
        print("nota inválida")
        nota2 = float(input("digite a sua nota da 2* avaliação: "))

    print(f"A sua média é: {(nota1+nota2)/2}")

    resposta=str(input("deseja continuar?\n(A resposta só pode ser sim e não)"))