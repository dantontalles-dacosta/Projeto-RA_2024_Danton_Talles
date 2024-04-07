con = 0
acm = 0
num = int(input("Insira um número inteiro positivo: "))

while (con <= num):
    if con % 2 == 0:
        acm += con
        con += 1
    else:
        con += 1

print(acm)