vetorUsuario = []
elementoInserir = 0
elementoApagar = 0
cont = 1


while cont != 0:
    inputUsuario = int(input("Insira 1 para adicionar um valor, 2 para apagar um valor e 0 para encerrar: "))
    if inputUsuario == 0:
        cont = 0
        print(vetorUsuario)
    elif inputUsuario == 1:
        elementoInserir = int(input("Insira o valor a adicionar: "))
        vetorUsuario.append(elementoInserir)
    elif inputUsuario == 2:
        elementoApagar = int(input("Insira o valor a remover: "))
        vetorUsuario.remove(elementoApagar)