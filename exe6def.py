#Crie uma função que calcule o fatorial de um número (sem usar recursão).
def fatorial(num):
    if num < 0:
        return None
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado    
print(fatorial(5))        