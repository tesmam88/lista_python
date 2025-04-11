#Faça um programa que leia tres numeros e mostre o maior e o menor deles
num1 = int(input("Digite numero 1: "))
num2 = int(input("Digite numero 2: "))
num3 = int(input("Digite numero 3: "))

if num1 > num2 and num1>num3 and num2>num3 :
    print("O numero",num1,"é o maior e o menor é",num3)
if num1 > num2 and num1>num3 and num3>num2:
    print("O numero",num1,"é o maior e o menor é",num2)    
elif num2 > num1 and num2>num3 and num3>num1:
    print("O numero",num2,"é o maior e o menor é",num1)
elif num2 > num1 and num2>num3 and num1>num3:
    print("O numero",num2,"é o maior e o menor é",num3)    
elif num3> num1 and num3>num2 and num1>num2:
    print("o numero",num3,"é o maior e o menor é",num2)
elif num3> num1 and num3>num2 and num2>num1:
    print("o numero",num3,"é o maior e o menor é",num1)  
else:
    print("comando invalido")              