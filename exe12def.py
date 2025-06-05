
def tempertura(celsius):
  farenheit = (celsius*9/5)+32
  return farenheit
  
c = float(input("Digite os graus em celsius: "))
print(tempertura(c))
