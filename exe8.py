#faça um programa que pergunte o preço de tres produtos e informe qual produto voce deve comprar, sabedendo que a decisão é pelo mais barato.
produto1 = float(input("Digite o preço do produto: "))
produto2 = float(input("Digite o preço dosegundo produto: "))
produto3 = float(input("Digite o preço doterceiro produto: "))

if produto1 < produto2 and produto1< produto3:
    print("O produto1 é o que deve ser comprado com valor de",produto1)
elif produto2 < produto1 and produto2 < produto3:
    print("O produto2 é o que deve ser comprado com valor de",produto2)
elif produto3 < produto1 and produto3 < produto2:
    print("O produto3 é o que deve ser comprado com o valor de",produto3)        

