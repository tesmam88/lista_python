hora = float(input("Digite o valor da sua hora: "))
qnt = float(input("Diga a quantidade de horas trabalhadas: "))
salario_bruto = hora*qnt
print("O salario bruto é de: ",salario_bruto)

if salario_bruto <= 900:
    ir = 0
    inss = 0
    fgts = salario_bruto*0.11
    total_desconto = ir + inss
    print("Isento de IMposto")

    salario_total = salario_bruto - total_desconto
if (salario_bruto >=901)  and (salario_bruto  <=1500) :
    ir = salario_bruto*0.05
    inss = salario_bruto*0.10
    fgts = salario_bruto*0.11
    total_desconto = ir + inss
    print("Imposto de 5%")
    salario_total = salario_bruto - total_desconto
elif salario_bruto >= 1501 and salario_bruto <=2499:
    ir = salario_bruto*0.10
    inss = salario_bruto*0.10
    fgts = salario_bruto*0.11
    total_desconto = ir + inss
    print("Imposto de 10%")
    salario_total = salario_bruto - total_desconto 
elif salario_bruto >=2500:
    ir = salario_bruto*0.20
    inss = salario_bruto*0.10
    fgts = salario_bruto*0.11
    total_desconto = ir + inss
    print("IMposto de 20%")     
    salario_total = salario_bruto - total_desconto

print("IR: ",ir)
print("INSS: ",inss)
print("FGTS: ",fgts)
print("Total de Descontos: ",total_desconto)
print("Salario Liquido:",salario_total)


