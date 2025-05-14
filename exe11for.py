#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
#Preço do pão: R$ 0.18
#Panificadora Pão de Ontem - Tabela de preços
#1 - R$ 0.18
#2 - R$ 0.36
#50 - R$ 9.00

print('---Panificadora Pão de Ontem ---')

cliente = 0
for i in range (1, cliente + 1):
    print(f'cliente: {cliente}')

quantidade = int(input('Numero de pães que o cliente levou: '))
if 1 <= quantidade <= 50:
    preco_total = quantidade*0.18
    print(f'O preço total de {quantidade} pães é de {preco_total}')

else:
    print('Quantidade invalida')    