class Ingresso():
    def __init__(self,valor):
        self.valor = valor

    def imprimeValor(self,valor):
        print(f"O valor do ingresso é {valor}")

class IngressoVIP(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
        self.valor = valor

    def imprimeValor(self,taxa):
        print(f"O valor do ingresso é {self.valor+self.valor*(taxa)/100}")

#teste

ingressoLP=IngressoVIP(100)
ingressoLP.imprimeValor(10)







