#

numero = int(input("Digite o numero de onde quer comecar a contagem: "))
numero2 = int(input("Digite o numero da tabuada  que deseja: "))
final = int(input("Digite o numero final da tabuada: "))


for i in range(numero2, final + 1):
    print(f"{numero} x {i} = {numero * i}")











