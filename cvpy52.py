numero = int(input("Digite um número: "))

quantidade_divisiveis = 0
for cada_numero in range(1, numero + 1):
    divisivel = numero % cada_numero == 0
    if divisivel:
        quantidade_divisiveis += 1
        print("\033[32m", end=" ")
    else:
        print("\033[m", end=" ")
    print(cada_numero, end=" ")

print(f"\033[m\nEsse número é divisível por {quantidade_divisiveis} números.")
if quantidade_divisiveis > 2:
    print("Este número NÃO é primo.")
else:
    print("Este número é primo.")
