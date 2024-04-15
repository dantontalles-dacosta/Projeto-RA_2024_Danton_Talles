primeiroCan = 0
segundoCan = 0
terceiroCan = 0
totalEleitores = int(input("Insira o total de eleitores: "))
voto = 0
contador = 0

while contador < totalEleitores:
    voto = int(input("Em qual candidato você quer votar? Insira 1 para o primeiro, 2 para o segundo e 3 para o terceiro: "))
    if voto == 1:
        print("Você votou no primeiro candidato.")
        primeiroCan += 1
        contador += 1
    elif voto == 2:
        print("Você votou no segundo candidato.")
        segundoCan += 1
        contador += 1
    elif voto == 3:
        print("Você votou no terceiro candidato.")
        terceiroCan += 1
        contador += 1

print(f"Primeiro candidato: {primeiroCan}, segundo candidato: {segundoCan} e terceiro candidato: {terceiroCan}.")