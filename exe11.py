#Faça um programa para a leitura de duas notas parciais de um aluno. O programa dever calcular a media alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a media for maior ou igual a sete,"Reporvado" for menor a sete e "Aprovado com Distinção", se media for igual a 10
nota1 = float(input("Digite a primerira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
if media >= 7 and media <=9.9:
    print("Aprovado com media",media)
elif media <=6.9:
    print("Reprovado com media",media)
elif media == 10:
    print("Aprovado com Distinção",media)
             