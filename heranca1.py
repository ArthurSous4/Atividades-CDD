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

------------------------------------------------

class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0
        
class Retangulo(Forma):
    def __init__(self,base,altura):
        super().__init__()
        self.base = base
        self.altura = altura
        
    def calcularArea(self,base,altura):
        resulArea = base * altura 
        
    def calcularPeri(self,base,altura):
        resulPeri= base*2+altura*2
        
class Triangulo(Forma):
    def __init__(self,base,altura,):
        super().__init__()
        self.base = base
        self.altura = altura

