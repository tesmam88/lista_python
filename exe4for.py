#ALTERE O PROGRAMA ANTERIOR PARA MOSTRAR NO FINAL A SOMA DOS NUMEROS.
x = int(input("Digite um numero: "))
y = int(input("Digite outro numero:"))
soma = 0
for i in range(x+1,y):
    print(i)
    soma += i
    print(f'{soma}')