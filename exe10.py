salario = float(input("Digite seu salario: "))
if salario <= 280.55:
    salario_reajuste = salario*0.2251+salario
    valor_aumneto = salario*0.2251
    percentual_aumneto = 0.2251
if salario >280.55 and salario <=709.72:
    salario_reajuste = salario*0.1539+salario
    valor_aumneto = salario*0.1539
    percentual_aumneto =0.1539
elif salario >709.73 and salario <=1501.33:
    salario_reajuste = salario*0.1097+salario
    valor_aumneto = salario*0.1097
    percentual_aumneto =0.1097
elif salario >1501.34:
    salario_reajuste = salario*0.519+salario
    valor_aumneto = salario*0.519
    percentual_aumneto =0.519        

print("O salario é: ",salario)
print("O percentual de aumento é: ",percentual_aumneto)
print("O vslor de aumento: ",valor_aumneto)
print("O salario fica em: ",salario_reajuste)  

