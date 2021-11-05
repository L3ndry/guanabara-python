valores = list()
continuando = True
while continuando:
    valor = int(input("Digite um valor: "))
    if valor not in valores:
        valores.append(valor)
    else:
        print("Valor duplicado! Não irei pôr na lista.")

    while True:
        resposta = input("Deseja continuar? [S/N] ").strip().upper()
        if resposta in "SS":
            break
        elif resposta in "NN":
            continuando = False
            break
        else:
            print("Oops! Valor inválido! Digite novamente.")

pares = list()
impares = list()
for cada_valor in valores:
    if cada_valor % 2 == 0:
        pares.append(cada_valor)
    else:
        impares.append(cada_valor)

print(f"A lista conpleta é {valores}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")
