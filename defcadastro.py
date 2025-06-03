def cadastro():
    x = input("diga seu nome: ")
    y = input('diga sua idade:')
    return x,y
print('iniciando cadastro...')
nome,idade = cadastro()
print('cadastro realizado com sucesso: ')
print('Seu nome é',nome,'e voce tem',idade,'anos de idade.')