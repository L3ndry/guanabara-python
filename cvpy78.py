valores = list()
maior = menor = 0

for contador in range(5):
    valores.append(int(input(f"Digite um valor para a posição {contador + 1}: ")))
    if contador == 0:
        maior = menor = valores[contador]
    else:
        if valores[contador] > maior:
            maior = valores[contador]
        elif valores[contador] < menor:
            menor = valores[contador]

print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {maior} na(s) posição(ões):", end=" ")
for posicao, valor in enumerate(valores):
    if valor == maior:
        print(posicao + 1, end="... ")
print(f"\nO menor valor digitado foi {menor} na(s) posição(ões):", end=" ")
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(posicao + 1, end="... ")
