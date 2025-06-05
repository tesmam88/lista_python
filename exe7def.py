#Crie uma função que receba um número e retorne True se ele for primo.
def primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    elif num == 3 or num == 5 or num == 7:
        return True
    elif num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    else:
        return True
    
print(primo(2))
print(primo(3))
print(primo(5))
print(primo(7))