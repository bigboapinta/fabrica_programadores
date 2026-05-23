#
nome = input("digite seu nome: ")
telefone = input(" me informe seu telefone:")
cidade = input(" me informe sua cidade:")
salario =int(input(" me informe sua renda mensal:"))

if salario > 1000:
    print(f" {nome}, voce possui uma renda mensal boa ")
elif salario > 700 and salario <= 1000:
    print(f" {nome}, voce possui uma renda mensal razoalvel")
elif salario > 500 and salario <= 700:
    print(f" {nome}, voce possui uma renda mensal baixa")
elif salario < 500:
    print(f" {nome}, voce possui uma renda mensal muito baixa")
else:
    print(f" {nome}, voce possui uma renda mensal baixa")


