'''
saida:
0
01
012
0123
'''

numero=int(input("digite um numero: "))

for x in range(0,numero+1):
    for y in range(x):
        print (y,end="")
    print()