salarioAtual = float(input("Insira seu salário atual: "))
anosServiço = float(input("Insira seu tempo de serviço em anos: "))

if anosServiço > 5:
    salarioBonus = salarioAtual * 1.05
    bonus = salarioBonus - salarioAtual
    print("Você tem direito a um bônus de ", bonus, ", elevando seu salário para R$", salarioBonus)
else:
    print("Você não tem direito ao bônus.")