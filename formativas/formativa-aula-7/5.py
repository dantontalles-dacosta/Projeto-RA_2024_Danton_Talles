baseFatorial = int(input("Insira um número inteiro: "))
calculoFatorial = baseFatorial
contador = baseFatorial - 1

while (contador > 0):
    calculoFatorial = calculoFatorial * contador
    contador -= 1

print(calculoFatorial)