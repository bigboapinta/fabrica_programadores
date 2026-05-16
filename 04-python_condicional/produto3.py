#
nome = input("Digite seu nome: ")

# Pedir a idade
idade = int(input("Digite sua idade: "))

produto = float(input("Digite o preço do produto: "))


if produto >= 100:
    preco = produto * 0.10
else:
    preco = produto * 0.05

# Mostrar resultado
print("\nNome:", nome)
print("Idade:", idade)
print("Valor calculado:", preco)























