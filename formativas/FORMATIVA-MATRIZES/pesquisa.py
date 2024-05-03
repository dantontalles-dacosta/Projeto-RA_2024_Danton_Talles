import numpy as np

## Exercício 1.

A = []

for i in range (10):
    linha = []
    for j in range(10):
        elemento = i * j - 2
        linha.append(elemento)
    A.append(linha)

print("As matrizes são iguais? Resposta: ", np.array_equal(np.transpose(A), A))

## Exercício 2.

M = ([[2,0,0],
      [0,5,0],
      [0,0,3]])

print("\nQual a soma dos elementos da diagonal principal da matriz M? Resposta: ", np.trace(M))