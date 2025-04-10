#Faça um programa que recebendo um valor inteiro, informe se o numero é positivo, negativo ou neutro
valor = int(input("Digite um valor inteiro: "))
if valor > 0:
    print("O valor",valor,"é positivo")
elif  valor == 0:
    print("O valor",valor,"é neutro")
else:
    print("O valor",valor,"é negativo")        