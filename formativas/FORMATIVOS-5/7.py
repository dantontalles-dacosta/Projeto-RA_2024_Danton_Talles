idade = int(input("Insira sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 18 and idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")