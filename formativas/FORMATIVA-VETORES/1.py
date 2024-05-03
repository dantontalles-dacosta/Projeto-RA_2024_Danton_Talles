vetorInt = [10,20,30,40,50]
indiceVetor = int(input("Insira o índice a consultar: "))

if indiceVetor >= 0 and indiceVetor < len(vetorInt):
    print(vetorInt[indiceVetor])
else:
    print("O índice está fora dos limites.")