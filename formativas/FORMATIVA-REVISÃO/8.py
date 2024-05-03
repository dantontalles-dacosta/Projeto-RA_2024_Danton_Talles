nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
salario = float(input("Insira seu salário: "))
sexo = str(input("Insira seu sexo (m para masculino, f para feminino): ")).lower()
estadoCivil = str(input("Insira seu estado civil (c para casado, s para solteiro, v para viúvo e d para divorciado): ")).lower()

if len(nome) < 3:
    print("O nome inserido não é válido, ele deve ter mais de três letras.")

if idade > 150 or idade < 0:
    print("A idade inserida não é válida, ela deve ser entre 0 e 150 anos.")

if salario <= 0:
    print("O salário inserido não é válido, ele deve ser maior que zero.")

if sexo != "f" and sexo != "m":
    print("O sexo informado é inválido, ele deve ser as letras f ou m.")

if estadoCivil != "c" and estadoCivil != "s" and estadoCivil != "v" and estadoCivil != "d":
    print("O estado civil inserido é inválido, ele deve ser as letras s, c, v ou d.")

