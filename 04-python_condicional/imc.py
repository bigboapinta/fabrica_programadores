#
nome = input("digite o seu nome:")
idade = int(input("digite  a sua idade:"))
altura = float(input("digite a sua altura:"))
peso = float(input("digite o seu peso:"))

imc = peso / (altura*altura)

if imc <= 18.5:
    print(" seu peso esta otimo")
 
   
else:
    print(" voce esta acima do peso, cuidado com a saude")
