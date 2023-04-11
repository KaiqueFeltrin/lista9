S = input("Digite uma palavra ou frase: ")

N_S = ""

for letra in S:
    if letra.lower() not in "aeiou":
        N_S += letra

print("A nova string sem vogais é:", N_S)