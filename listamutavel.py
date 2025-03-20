#strings sao imutaveis / listas sao mutaveis
frutas = ['banana','maça','cereja']
frutas[0] = 'pera'
frutas[-1] = 'laranja'
print(frutas)

# lista mutavel com mais de uma lista
uma_lista = ['a','b','c','d','e','f']
uma_lista[1:3] = ['x','y']
print(uma_lista)

#remoçaõ de elementos de uma lista

uma_lista = ['a','b','c','d','e','f']
print(uma_lista)
print(len(uma_lista))

uma_lista[1:3] = []
print(uma_lista)
print(len(uma_lista))

#inserir elemento em uma lista
uma_lista = ['a','d','f']
uma_lista [1:1] = ['b','c']
print(uma_lista)
uma_lista[4:4] = ['e']
print(uma_lista)