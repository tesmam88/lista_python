print ('-----PASSAGEM AEREA-----')

print('-- CADASTRO CLINTE --')
cadastro_cliente = []
nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
rg = int(input('RG: '))
cpf = int(input('CPF: '))
endereco = input('Endereço: ')
fone = input('telefone: ')
idade = int(input('Idade: '))

cliente = [nome,sobrenome,rg,cpf,endereco,fone,idade]
cadastro_cliente.append(cliente)
print(cliente)

print('-- CADASTRO PASSAGEM --')
cadastro_passagem = []
destino = input('Destino: ')
origem = input('Origem: ')
duracao = float(input('Horas de voo:'))
valor_passagem = float(input('Valor da Passagem: '))
desconto = 5/100

passagem = [destino,origem,duracao,valor_passagem,desconto]
cadastro_passagem.append(passagem)
print(passagem)

print('-- CADASTRO DE AVIÃO --')
cadastro_aviao = []
modelo = input('Modelo do avião: ')
ano = int(input('Ano do modelo: '))
horas = float(input('Horas de voo: '))
cor = input('cor do avião: ')
capacidade = int(input('Quantidade de passageiros: '))

aviao = [modelo,ano,horas,cor,capacidade]
cadastro_aviao.append(aviao)
print(aviao)

print('-- CADASTRO DE TRIPULAÇÃO --')
cadastro_tripulacao = []
nome_trip = input('Nome tripulante: ')
descricao_cargo = input('Descrição do Cargo: ')
idade_trip = int(input('Idade: '))
data_emissao = input('Data de Emissão: ')
fone_trip = int(input('telefone: '))

tripulacao = [nome_trip,descricao_cargo,idade_trip,data_emissao,fone_trip]
cadastro_tripulacao.append(tripulacao)
print(tripulacao)


