listaInteiros = [1,2,3,4,5]
numRemove = int(input("Insira o número a remover: "))

for i in listaInteiros:
    if i == numRemove:
        listaInteiros.remove(numRemove)

print(listaInteiros)