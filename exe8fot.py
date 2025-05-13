#faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a media de idade da turma varia entre 0 e 25,26 e 60 e maior que 60.
#e então dizer se a turma é jovem, adulta ou idosa, comforme a média calculada. Usando for

idades = 0
n = int(input("Digite o numero de pessoas: "))

for i in range(1, n +1):
    idade = int(input(f"Digite a sua idade {i}: "))
    idades += idade

media = idades/n

if media <= 25:
 classificação = 'jovem'
elif media <=26 and media <=60:
 classificação = 'adulta'
else:
  classificação = 'idosa'

print(f"\n A media de idades é {media:}anos ")
print(f"\n Classificação da turma {classificação}")      