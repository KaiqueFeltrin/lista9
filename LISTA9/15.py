P = input("Digite uma palavra de até 10 caracteres: ")
V = "aeiouAEIOU" # Definindo as vogais

num_V = 0
for letra in P:
    if letra in V:
        num_V += 1

print("A palavra", P, "possui", num_V, "vogais.")