#Fazer um algoritmo que recebe o salario atual de um funcionario, calcule o valor do novo salario reajustando de acordo com a tabela abaixo:
#Abaixo de R$500 Reajuste 15%, de R$500 ate 1000 Reajuste 10%, Acima de R$1000 Reajuste 5%
salario_atual = float(input("Digite o seu salario atual: "))

if salario_atual <= 500:
    salario_novo = salario_atual*0.15+salario_atual
    print("Seu novo salario é de:",salario_novo)

elif salario_atual >500 and 1000:
    salario_novo = salario_atual*0.10+salario_atual
    print("Seu novo salario é de:",salario_novo)
else :
    salario_novo = salario_atual*0.5+salario_atual
    print("Seu novo salario é de:",salario_novo)  
