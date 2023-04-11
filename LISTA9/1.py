p = input("Digite uma palavra de até 10 caracteres: ")
v = "aeiouAEIOU" # Definindo as vogais

num_v = 0
for letra in p:
    if letra in v:
        num_v += 1

print("A palavra", p, "possui", num_v, "vogais.")