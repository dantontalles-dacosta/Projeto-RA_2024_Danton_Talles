vetorInt = []
somaVetor = 0
cont = 1

while cont != 0:
    valorInserir = int(input("Insira 1 para adicionar um valor e 0 para encerrar: "))
    if valorInserir == 0:
        cont = 0
    elif valorInserir == 1:
        vetorInt.append(int(input("Insira o valor a adicionar: ")))

for i in vetorInt:
    somaVetor = somaVetor + i

print(somaVetor)