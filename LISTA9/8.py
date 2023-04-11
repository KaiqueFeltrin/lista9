N = input("Digite o nome da pessoa: ")
S = input("Digite o sexo da pessoa (M ou F): ")
I = int(input("Digite a idade da pessoa: "))

if S == "F" and I < 25:
    print(N + " ACEITA")
else:
    print("NÃO ACEITA")