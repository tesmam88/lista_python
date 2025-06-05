clientes = []


nome = input("Digite seu nome: ")
cpf = int(input("\nDigite seu cpf: \n"))
rg = int(input("\nDigite seu rg: \n"))
telefone = int(input("\nDigite seu numero de telefone: \n"))
agencia = int(input("\nDigite a agencia do banco: \n"))
conta = int(input("\nDigite a conta: \n"))


while True:
  try:
    saldo_inicial = float(input("\nDigita o saldo inicial: \n"))
    if saldo_inicial <= 0:
      print("O saldo não pode ser negativo")
    else:
      break  
  except ValueError:
    print("Não digite um valor invalido")

cliente = [nome,cpf,rg,telefone,agencia,conta,saldo_inicial]
clientes.append(cliente)
print(cliente)



