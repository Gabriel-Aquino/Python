from segunda.Class2 import Estoque

p1 = Estoque("Sabao", 100, 1)

print(p1.descricao())

p1.darbaixa(10)
print(p1.descricao())

if(p1.precisarepor() == False):
    print ("Não precisa repor")
else:
    print("Precisa repor")