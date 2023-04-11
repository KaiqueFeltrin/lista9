VA = list("COMPUTACAO")

VB = input("Digite uma palavra de 10 letras: ")

VB = VB.upper()

for i in range(len(VA)):
    if VA[i] == VB[i]:
        print(f"A letra '{VB[i]}' está na posição {i} de vetB.")