temporario = list()
principal = list()
maior = menor = 0
while True:
    temporario.append(input("Nome: ").strip().title())
    temporario.append(float(input("Peso: ")))

    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        elif temporario[1] < menor:
            menor = temporario[1]

    principal.append(temporario[:])
    temporario.clear()

    resposta = input("Deseja continuar? [S/N] ").strip().upper()
    if resposta == "N":
        break
    if resposta == "S":
        print("Continuando...")
    else:
        break

print(f"Ao todo, você cadastrou {len(principal)} pessoas.")
print(f"O maior peso foi {maior}Kg. Peso de", end=" ")
for pessoa in principal:
    if pessoa[1] == maior:
        print(pessoa[0], end=" ")
print(f"\nO menor peso foi de {menor}Kg. Peso de", end=" ")
for pessoa in principal:
    if pessoa[1] == menor:
        print(pessoa[0], end=" ")
