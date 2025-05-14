#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
#50 - R$ 99.50
print('---Loja quase Dois - Tabela de Preços---')

num_clientes = int(input("Diga o numero de clientes atendidos: "))

for i in range(1, num_clientes+1):
    print(f'cliente: {i}')
    quantidade = int(input('Numero de itens que o cliente levou(1 - 50) '))
    if 1 <= quantidade <=50:
        preco_total = quantidade*1.99
        print(f'total a pagar: {preco_total:.2f}')
    else:
        print('quantidade invalida')    
