primeiroNum = int(input("Insira o primeiro número: "))
segundoNum = int(input("Insira o segundo número: "))
terceiroNum = int(input("Insira o terceiro número: "))

if primeiroNum > segundoNum and primeiroNum > terceiroNum:
    print(primeiroNum)
elif segundoNum > primeiroNum and segundoNum > terceiroNum:
    print(segundoNum)
else:
    print(terceiroNum)