'''
problema: digite um numero 5
saída: 122333444455555
'''


numero=int(input("digite um numero: "))

for x in range(numero+1):
    for y in range(x):
        print (x,end="")  ##  <--  IMPORTANTE
    print()

