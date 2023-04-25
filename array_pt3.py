vetorprim=[]
vetorsec=[]
vetorterc=[]

qntdd=int(input("digite a quantidade de operações: "))

for i in range(qntdd):
    vetorprim.append(int(input("digite um número")))
    vetorsec.append(int(input("digite um número")))

for j in range(qntdd):
    vetorterc.append(vetorprim[j] + vetorsec[j])

print(vetorprim)
print(vetorsec)
print(vetorterc)