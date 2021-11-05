contador = soma = maior_valor = menor_valor = 0
continuar = True
while continuar:
    numero = int(input("Digite um número inteiro: "))
    contador += 1
    soma += numero
    if contador == 1:
        maior_valor = menor_valor = numero

    if numero > maior_valor:
        maior_valor = numero
    elif numero < menor_valor:
        menor_valor = numero

    pergunta = input("Quer continuar? [S/N] ").upper().strip()
    if pergunta == "N":
        continuar = False

media = soma / contador
print(f"Você digitou {contador} números e a média foi {media}")
print(f"O maior valor digitado foi {maior_valor} e o menor foi {menor_valor}.")
