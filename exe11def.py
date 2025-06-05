#Crie uma função que receba um número e retorne uma lista com todos os divisores dele.
def numero(n):
  lista_num = []
  for i in range (1, n + 1):
      if n % i == 0:
        lista_num.append(i)
  return lista_num
x = int(input("Digite um numero: "))
print(numero(x))        
