senha = input("Insira sua senha: ")
nomeUsuario = input("Insira seu nome de usuário: ")

while senha == nomeUsuario: 
    print("Sua senha e nome de usuário não podem ser iguais, por favor insira valores diferentes.")
    senha = input("Insira sua senha: ")
    nomeUsuario = input("Insira seu nome de usuário: ")

print("Senha e nome de usuário cadastrados.")