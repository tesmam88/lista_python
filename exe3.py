#Faça um algoritmo que receba duas notas e calcule a media aritmetica e mostre o resultado.
nota1 = float(input("Diga a nota1: "))
nota2 = float(input("Diga a nota2: "))
media = nota1+nota2/2

if media >= 7.0:
    print("Aluno Aprovado com",media)
elif media <=7.0:
    print("Aluno Reprovado com",media)    