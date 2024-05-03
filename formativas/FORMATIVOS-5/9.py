salarioBruto = float(input("Insira seu salário: "))

if salarioBruto <= 20000:
    print("Seu salário está isento de imposto de renda.")
if salarioBruto > 20000 and salarioBruto <= 50000:
    imposto = salarioBruto * 0.15
    print("Seu salário será taxado em R$", imposto,", 15 por cento do seu salário")
else:
    imposto = salarioBruto * 0.25
    print("Seu salário será taxado em R$", imposto,", 25 por cento do seu salário")