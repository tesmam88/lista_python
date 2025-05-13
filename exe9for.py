#NUma eleição existem 3 candidatos. Faça um programa que peça o numero total de eleitores. Peça para cada eleitor votar e ao final mostrar o numero de votos de cada candidato.
#Mostre tambem o candidato campeão.
candidato1 = 0
candidato2 = 0
candidato3 = 0
eleitores = int(input("Digite o numero total de eleitores: "))
for i in range(1, eleitores + 1):
    voto = int(input("Digite seu voto(13,17,50): "))
   
    if voto == 13:
        candidato1 += 1
        print('Faz o L')
    elif voto == 17:
        candidato2 += 1
        print('Bozo')
    elif voto == 50:
        candidato3 += 1
        print('Danilo Gentili')

print("---Resultado da Eleição---")
print(f'candidato1: {candidato1} votos\n')
print(f'candidato2: {candidato2} votos\n') 
print(f'candidato 3: {candidato3} votos\n')       

if candidato1 > candidato2 and candidato1 > candidato3:
        print('Voce é o candidato vencedor - Lula',candidato1)
elif candidato2 > candidato1 and candidato2 > candidato3:
        print('Voce é o candidato campeão!!! - Bolsonaro',candidato2)
elif candidato3 > candidato2 and candidato3 > candidato1:
        print('voce é o vencedor!! - Danilo Gentili',candidato3)                        