N = int(input("Digite o número de termos da sequência de Fibonacci que você deseja imprimir: "))

termo1 = 0
termo2 = 1
contador = 0

if N <= 0:
    print("Por favor, insira um número inteiro positivo.")
elif N == 1:
    print("Sequência de Fibonacci com 1 termo:", termo1)
else:
    print("Sequência de Fibonacci com", N, "termos:")
    while contador < N:
        print(termo1, end=" ")
        termo_temp = termo1 + termo2
        termo1 = termo2
        termo2 = termo_temp
        contador += 1