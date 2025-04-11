#Faça um programa que leia tres numeros e mostreos em ordem decrescente
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite um novo numero: "))

if num1<num2 and num3<num2 and num1<num3:
    print("ordem de numeros decrescente é: ",num2,num3,num1)
if num1<num2 and num2<num3 and num1<num3:
    print("ordem de numeros decrescente é: ",num3,num2,num1)    
elif num2<num1 and num2<num3 and num1<num3:
    print("ordem de numeros decrescente é: ",num1,num3,num2)
elif num2<num1 and num2<num3 and num3<num1:
    print("ordem de numeros decrescente é: ",num3,num1,num2)   
elif num3<num1 and num3<num2 and num1<num2:
    print("ordem de numeros decrescente é: ",num2,num1,num3)
elif num3<num1 and num3<num2 and num2<num1:
    print("ordem de numeros decrescente é:",num1,num2,num3)            