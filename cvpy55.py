maior_peso = 0
menor_peso = 0

for cada_peso in range(0, 5):
    peso = float(input(f"Peso da {cada_peso + 1}ª pessoa: "))

    if cada_peso == 0:
        maior_peso = peso
        menor_peso = peso

    elif peso > maior_peso:
        maior_peso = peso

    elif peso < menor_peso:
        menor_peso = peso


print(f"O maior peso lido foi de {maior_peso}Kg.")
print(f"O menor peso lido foi de {menor_peso}Kg.")
