#Escreva uma função que verifique se um número é par.
def par(num):
    result = num % 2 == 0
    return result
a = int(input("Digite um numero: "))
resultado = par(a)
if resultado :
    print("o numero",a,"é par")
else:
    print("numero",a,"não par")
