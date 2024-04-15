primeiroNum = int(input("Insira o primeiro número: "))
segundoNum = int(input("Insira o segundo número: "))
somaTotal = 0

for i in range(primeiroNum + 1, segundoNum, 1):
    print(i)
    somaTotal = somaTotal + i
    if (i == segundoNum - 1):
        print(somaTotal)