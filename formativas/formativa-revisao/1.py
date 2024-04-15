nota = float(input("Insira uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Esse valor é invalido.")
    nota = float(input("Insira uma nota de 0 a 10: "))

if nota >= 0 and nota <= 10:
    print("Obrigado pela avaliação.")
