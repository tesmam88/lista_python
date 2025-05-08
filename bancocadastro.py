clientes = []

nome = (input("Digite seu nome: "))
cpf = int(input("Digite seu cpf: "))
rg = int(input("Digite seu rg: "))
telefone = int(input("Digite seu telefone: "))
agencia = int(input("Digite seu numero de agencia: "))
conta = int(input("Digite sua conta: "))
saldo = float(input("Saldo inicial: "))

cliente=[nome,cpf,rg,telefone,agencia,conta,saldo]

clientes.append(cliente)
print(cliente)

menu = input("EScolha uma opção: ")
saldo = 1 
depositar = 2
sacar = 3
sair =  4
if menu ==' 1':
    print("Saldo: {cliente[saldo]}")

if menu == 2:
    print("Depositar:")


