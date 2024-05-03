numero = int(input("Digite um número inteiro para iniciar a contagem regressiva: "))

if numero < 0:
    print("Por favor, insira um número inteiro não negativo.")
else:
    print("Contagem regressiva iniciando em", numero)
    
    while numero >= 0:
        print(numero)
        numero -= 1