class Funcionario(object):

    def __init__(self, nome, horas, valorh):
        self.nome = str(nome)
        self.horas = float(horas)
        self.valorh = float(valorh)

    def getnome(self):
        return (self.nome)
    def setnome(self, nome):
        self.nome = str(nome)

    def gethora(self):
        return (self.horas)
    def sethora(self, horas):
        self.horas = float(horas)

    def getvalor(self):
        return (self.valorh)
    def setvalor(self, valorh):
        self.valorh = float(valorh)


    def calcsalario(self):
        return (self.valorh*self.horas)