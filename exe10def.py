#Escreva uma função que conte quantas vogais há em uma string.
def contar(palavra):
  vogais = "aAeEiIoOuU"
  return sum (palavra.count(vogal) for vogal in vogais)
x = input("Digite uma palavra: ")
resultado = contar(x)
print("O numero de vogais foi",resultado)
