# Arquivo
soma = 0
num = int(input("Numero: "))
var = 0
while num != 0:
    soma += num
    var += 1
    num = int(input("Numero: "))
soma = soma/var
print("Total = ", soma)
