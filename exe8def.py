#Crie uma função que inverta uma string.
def inverter(frase):
      return ''.join(reversed(frase))
x = input("Escreva uma frase: ")
invertido = inverter(x)
print(invertido)
    