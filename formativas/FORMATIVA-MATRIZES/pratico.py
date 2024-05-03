import numpy as np

## Número 01.

A = np.eye(3)
print("\nExercício 1: \n", A)

## Número 02.

A = []
B = []

for i in range(2):
    linha = []
    for j in range(2):
        elemento = i + j
        linha.append(elemento)
    A.append(linha)
    
for i in range(2):
    linha = []
    for j in range(2):
        elemento = i - j
        linha.append(elemento)
    B.append(linha)

A = np.array(A)
B = np.array(B)

print("\nExercício 2: \n", np.dot(A,B))

## Número 03.

A = []

for i in range(3):
    linha = []
    for i in range(2):
        elemento = i * j
        linha.append(elemento)
    A.append(linha)

A = np.array(A)

print("\nExercício 3: \n", np.transpose(A))

## Número 04.

A = []
B = []

for i in range(2):
    linha = []
    for j in range(3):
        elemento = i - j
        linha.append(elemento)
    A.append(linha)

for i in range(2):
    linha = []
    for j in range(3):
        elemento = i + j
        linha.append(elemento)
    B.append(linha)

A = np.array(A)
B = np.array(B)

print("\nExercício 4: \n", A - B)

## Número 05.

A = []

for i in range(4):
    linha = []
    for j in range(4):
        elemento = i * i
        linha.append(elemento)
    A.append(linha)

A = np.array(A)

print("\nExercício 5: \n", A)