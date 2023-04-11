P = input("Digite uma palavra: ")
N_P = ""

for caractere in P:
    novo_valor_ascii = ord(caractere) + 1
    novo_caractere = chr(novo_valor_ascii)
    nova_P += novo_caractere

print("A nova palavra é:", nova_P)