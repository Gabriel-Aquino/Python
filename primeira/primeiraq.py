from primeira.Class1 import Funcionario

f1 = Funcionario("Zé do Pulo", 20, 4.50)
f2 = Funcionario("Paulo Preguiça", 10, 6.35)
f3 = Funcionario("Tonin Barca Furada", 40, 13.80)

print("Zé do Pulo ganha: ", f1.calcsalario(),"/H")
print("Paulo Preguiça Ganha: ", f2.calcsalario(),"/H")
print("Tonin Ganha: ", f3.calcsalario(),"/H")


a = 1
while(a < 4):
    b = str(input("Escreva o nome do Funcionario: "))
    c = float(input("Horas Trabalhadas: "))
    d = float(input("Valor da Hora: "))

    cad = Funcionario(b, c, d);
    print("Funcionario ",b," Recebe: ",cad.calcsalario(),"/H")
    a+=1