#Faça um programa que leia 5 numeros e informe a soma e a media dos numeros
y = 0
z = 0
for i in range (5):
    print("Digite",i+1,"1ero valor")
    x = int(input())
    y = y+x
    z = z+1
print(y)
print(y/z)