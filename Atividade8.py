alunos=int(input("quantos alunos existem na sala: "))
contador=0
soma=0
while contador != alunos:
    nota=float(input("qual é a nota do aluno: "))
    soma=soma+nota
    contador=contador+1

print(f"a media da sala é: {soma/alunos}")

