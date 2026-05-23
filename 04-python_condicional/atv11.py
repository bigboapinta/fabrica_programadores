#
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome}, você é maior de idade.")
    
    cnh = input("Você possui CNH? (sim/não): ")
    if cnh.lower() == "sim":
        print("Parabéns, você pode dirigir!")   
    else:
        print("Você não pode dirigir.")  
else:
    print(f"{nome}, você é menor de idade.")















