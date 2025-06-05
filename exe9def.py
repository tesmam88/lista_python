#Crie uma função que receba uma lista de nomes e retorne apenas os nomes com mais de 5 letras.
def filtro_nomes(lista_nomes):
  return [nome for nome in lista_nomes if len(nome) > 5]
x = ["Rafael","Renato","Joao","Pedro","Juca","Mateus"]
resultado = filtro_nomes(x)
print(resultado)