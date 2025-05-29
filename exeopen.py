#Crie um programa em Python que cadastre usuários com nome e idade, sexo, Endereço, Cidade e Estado, armazenando esses dados em listas e, ao final, salve todas as informações em um arquivo cadastro.txt.
#O Aplicativo deverá ter um módulo de consulta de todos os dados.
#Regras:
#Cadastro:
#O usuário pode cadastrar quantas pessoas quiser.
#O programa deve perguntar ao final de cada cadastro se deseja cadastrar outra pessoa.
#Use try e except para garantir valores válidos.
#Após encerrar os cadastros, grave os dados no arquivo cadastro.txt, no formato:
#Consultas:
#O usuário deverá consultar todos os dados do arquivo
#Sair
#Ao definir sair, o programa será encerrado e os dados preservados.
#Ex.
#Nome: Maria, Idade: 22, Sexo:F, Endereço: Rua Afonso Penas, 4995, Cidade: Campo Grande, Estado: MS
#-------------------------------------------------------------------------------------------------- 
#Nome: João, Idade: 30, Sexo:M, Endereço: Rua Afonso Penas, 4996, Cidade: Campo Grande, Estado: MS ...

usuarios = []

while True:

    try:

        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        sexo = input("Diga seu sexo: ")
        endereco = input("Digite seu endereço: ")
        cidade = input("Digite sua cidade: ")
        estado = input("Diga o estado: ")
        cpf = int(input("Digite seu cpf: "))

        usuario = [nome,idade,sexo,endereco,cidade,estado,cpf]
        usuarios.append(usuario)
        print(usuario)

        continua = input("Deseja cadastrar outra pessoa?(S/N)").strip().upper()
        if continua != "S":
            break
    except ValueError:
        print("Idade dever ser um numero inteiro")    



    