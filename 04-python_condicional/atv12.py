#
nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Nome: {nome}")
print(f"Média: {media:.2f}")

if media >= 7:
    print("Parabéns, você foi aprovado!")
elif media >= 4 and media > 7 :
    print("Você está de recuperação.")
else:
    print("Sinto muito, você foi reprovado.")






