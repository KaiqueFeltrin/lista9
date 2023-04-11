S = input("Digite a string: ")
C = 0

for char in S:
    if char == '1':
        C += 1

print("O número de ocorrências do caractere '1' na string é:", C)