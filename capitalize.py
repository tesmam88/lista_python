# Capitalizar - Transforma a primeira letra en maiuscula
a = "tesmam"
print(a.capitalize())

#Funcao upper - deixa tudo maiusculo (a = a.upper())
a = "tesmam"
print(a.upper())

#função lower()/casefold() - deixa em minuscula
a = "TESMAM"
print(a.casefold()) 

#função islower()/ isupper() - verdadeiro/falso
a = "TESMAM"
print(a.isupper())
print(a.islower())

#funcao isdigit() - verdadeiro/falso digitos
a= "12345"
print(a.isdigit())
a="123rtg"
print(a.isdigit())