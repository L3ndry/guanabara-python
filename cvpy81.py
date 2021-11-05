valores = list()
continuar = True
while continuar:
    valor = int(input("Digite um valor: "))
    valores.append(valor)
    while True:
        resposta = input("Quer continuar? [S/N] ").strip().upper()
        if resposta not in "SS" and resposta not in "NN":
            print("Oops! Valor inválido! Digite novamente.")
        else:
            if resposta in "NN":
                continuar = False
                break
            elif resposta in "SS":
                break

valores.sort(reverse=True)
print(f"Você digitou {len(valores)} elementos.")
print(f"Os valores em ordem decrescente são {valores}")
if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista.")
