sexo = input("Informe o seu sexo biológico: [M/F] ").upper()
while sexo != "M" and sexo != "F":
    sexo = input("Dados inválidos. Por favor, informe seu sexo: ").upper()

print(f"Sexo {sexo} foi registrado com sucesso!")
