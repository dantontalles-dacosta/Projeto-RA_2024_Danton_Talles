nota = float(input("Insira a nota do aluno: "))

if nota >= 9 and nota <= 10:
    print("A nota do aluno é A.")
elif nota >= 7 and nota <= 8.9:
    print("A nota do aluno é B.")
elif nota >= 5 and nota <= 6.9:
    print("A nota do aluno é C.")
elif nota < 5:
    print("A nota do aluno é D.")
else: 
    print("A nota inserida não é válida.")
