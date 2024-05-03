valorCompra = float(input("Insira o valor de sua compra: "))

if valorCompra >= 100:
    valorCompraDesconto = valorCompra * 0.90
    desconto = valorCompra - valorCompraDesconto
    print("Você ganhou um desconto de R$", desconto,", deixando sua compra final no valor de R$",valorCompraDesconto)