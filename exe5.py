#Faça um programa que verifique se uma letra digitada é "F", "M", "O". Conforme a letra escrever: F - femenino, M - masculino, O - outros ou sexo invalido.
sexo = input("Digite seu sexo (F,M ou O): ")
F = 'femenino'
M = 'masculino'
O = 'sexo indefinido'

if sexo == "F" or sexo == "f" :
    print("Sexo Femenino")
if sexo == "M" or sexo == "m" :
    print("Sexo Masculino")
elif sexo == "O" or "o":
    print("Sexo Invalido")        