with open("cadastro.txt","r") as f:
    linhas = f.readlines()
#remove a linha do indice 2(terceira linha)
del linhas[2]
with open("cadastro.txt","w")as f:
    f.writelines(linhas)
