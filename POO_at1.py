class Pessoa:
    def __init__(self,nome=str(),peso=float(),idade=int(),comendo=False,falando=False,dormindo=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.falando=falando
        self.dormindo=dormindo

    def comer(self,alimento):
        self.alimento=alimento
        if self.falando==True:
            print(f"{self.nome} não pode comer {alimento} enquanto fala")

        else:
            if self.comendo == False:
                print(f"{self.nome} Começou a comer {alimento}")
                self.comendo = True
            else:
                print(f"{self.nome} já está comendo")

    def parardecomer(self):
        if self.comendo==True:
            print(f"{self.nome} parou de comer")
            self.comendo = False

        else:
            print(f"{self.nome} não esta comendo")

    def falar(self):
        if self.dormindo==True:
            print(f"{self.nome} não pode falar enquanto está dormmindo")

        else:
            if self.comendo == True:
                print(f"{self.nome} não pode falar enquanto come")

            else:
                print(f"{self.nome} está falando")
                self.falando = True

    def parardefalar(self):
        if self.falando==True:
            print(f"{self.nome} parou de falar")
            self.falando=False

        else:
            if self.falando==False:
                print(f"{self.nome} não está falando")

    def dormir(self):
        if self.comendo==False and self.falando==False:
            print(f"{self.name} está dormindo")
            self.dormindo=True

        else:
            print(f"{self.name} não pode dormir se está falando e comendo")


    def acordar(self):
        if self.dormindo==True:
            print(f"{self.nome}está dormindo")
            self.dormindo=False

        else:
            print(f"{self.name} já esta acordado")


p1=Pessoa("Carlos",80,23,False)
p2=Pessoa("Maria",54,34,True)

p1.comer("laranja")
p1.falar()
p1.parardecomer()
p1.falar()
p1.comer('laranja')
p1.parardefalar()
