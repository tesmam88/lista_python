hora = float(input("Digite o valor da sua hora: "))
qnt = float(input("Diga a quantidade de horas trabalhadas: "))
salario_bruto = hora*qnt
print("O salario bruto é de: ",salario_bruto)
inss = salario_bruto*0.10
fgts = salario_bruto * 0.11


if salario_bruto <= 900:
    ir = 0
    inss = 0
    
    total_desconto = ir + inss
    print("Isento de IMposto")

salario_total = salario_bruto - total_desconto
if salario_bruto >=901  and salario_bruto  <=1500:
    ir = salario_bruto*0.05
    inss = salario_bruto*0.10
    total_desconto = ir + inss
    
salario_total = salario_bruto - total_desconto    
print("INSS: ",inss)
print("FGTS: ",fgts)
print("Total de Descontos: ",total_desconto)
print("Salario Liquido:",salario_total)


