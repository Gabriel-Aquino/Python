class Paciente(object):

    def __init__(self, nome, peso, altura):
        self.nome = str(nome)
        self.peso = float(peso)
        self.altura = float(altura)

    def getnome(self):
        return self.nome
    def setnome(self, nome):
        self.nome = str(nome)

    def getpeso(self):
        return self.peso
    def setpeso(self, peso):
        self.peso = float(peso)

    def getaltura(self):
        return self.altura
    def setaltura(self, altura):
        self.altura = float(altura)

    def IMC(self):
        form = float(self.peso * (self.altura*self.altura))
        return form
