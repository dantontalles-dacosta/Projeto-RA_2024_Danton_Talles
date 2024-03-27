lado1 = float(input("Insira o valor do primeiro lado do triângulo: "))
lado2 = float(input("Insira o valor do segundo lado do triângulo: "))
lado3 = float(input("Insira o valor do terceiro lado do triângulo: "))

if lado1 == lado2 == lado3:
    print("Esse triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Esse triângulo é isósceles.")
else:
    print("Esse triângulo é escaleno.")