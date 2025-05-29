with open("cadastro.txt","r")as f:
    for linha in f:
        if "joão"in linha.lower():
            print(linha)