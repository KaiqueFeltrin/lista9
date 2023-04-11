F = "Esta é uma frase de exemplo."
C = 0

for caractere in F:
    if caractere.isspace():
        C += 1

print("A frase tem", Contador, "caracteres em branco.")