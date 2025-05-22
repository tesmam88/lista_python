
try:
    a = int(input("Digite uma palavra: "))
except ValueError:
    print("Digite apenas numeros")    
except:
    print("Erro desconhecido")    
finally:
    print('final do algoritmo')
