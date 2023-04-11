P = input("Digite uma palavra: ")
V = 'aeiou'
N_V = 0

for letra in palavra:
    if letra.lower() in V:
        N_V += 1

substituir = input("Digite um caractere para substituir as vogais: ")

nova_P = ""
for letra in P:
    if letra.lower() in V:
        nova_P += substituir
    else:
        nova_P += letra

print("A palavra", P, "possui", N_V, "vogais.")
print("Nova palavra:", nova_P)