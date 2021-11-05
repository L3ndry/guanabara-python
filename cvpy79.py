valores = list()

rodando = True
while rodando:
    valor = int(input("Digite um valor: "))
    if valor in valores:
        print("Valor duplicado! Não irei adicionar...")
    else:
        valores.append(valor)
        print("Valor adicionado com sucesso...")

    while True:
        continuar = input("Deseja continuar? [S/N] ").upper().strip()
        if continuar == "N" or continuar == "NAO" or continuar == "NÃO":
            rodando = False
            break
        elif continuar == "SIM" or continuar in "SS":
            break
        else:
            print("Oops! Valor inválido! Digite novamente.")

print(f"Você digitou os valores {sorted(valores)}")
