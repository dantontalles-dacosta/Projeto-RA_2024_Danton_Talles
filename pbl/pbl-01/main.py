print("Essa é uma calculadora de imposto de renda.")
salario = float(input("Insira seu salário: "))

if salario >= 2259.21 and salario <= 2826.65:
    imposto = salario * 0.075 + 169.44
    print("Você pagará 7,5 por cento da alíquita de imposto, totalizando R$", imposto,"que serão abatidos do seu salário.")
elif salario >= 2826.66 and salario <= 3751.05:
    imposto = (salario * 0.15) + 381.44
    print("Você pagará 15 por cento da alíquita de imposto somado ao valor base da sua faixa, totalizando R$", imposto,"que serão abatidos do seu salário.")
elif salario >= 3751.06 and salario <= 4664.68:
    imposto = (salario * 0.225) + 662.77 
    print("Você pagará 22,5 por cento da alíquita de imposto somado ao valor base da sua faixa, totalizando R$", imposto,"que serão abatidos do seu salário.")
elif salario > 4664.68:
    imposto = (salario * 0.275) + 896.00
    print("Você pagará 27 por cento da alíquita de imposto somado ao valor base da sua faixa, totalizando R$", imposto,"que serão abatidos do seu salário.")
else:
    print("Você está isento do imposto de renda.")