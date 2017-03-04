class Estoque(object):

    def __init__(self, nome, qt, qtm):
        self.nome = str(nome)
        if (qt > 0):
            self.qt = int(qt)
        if (qtm > 0):
            self.qtm = int(qtm)

    def getnome(self):
        return self.nome
    def setnome(self, nome):
        self.nome = nome

    def getqt(self):
        return self.qt
    def setqt(self, qt):
        self.qt = qt

    def getqtm(self):
        return self.qtm
    def setqtm(self, qtm):
        self.qtm = qtm

    def repor(self, qtd):
        soma = self.getqt()
        soma += qtd
        self.setqt(soma)

    def darbaixa(self, qtd):
        dim = self.getqt()
        dim -= qtd
        if(dim < 0):
            print("Erro! Nada foi Reajustado")
            self.getqt()
        self.setqt(dim)

    def descricao(self):
        prod = str("Produto: %s, Quantidade: %i, Quantidade Mínima: %i" %(self.getnome(), self.getqt(), self.getqtm()))
        return prod

    def precisarepor(self):
        return self.getqtm() < self.getqtm()

