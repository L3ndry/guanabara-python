print("Sequência de Finobacci")
print("-" * 15)
quantidade = int(input("Quantos termos você quer mostrar? "))

termo1 = 0
termo2 = 1
termo3 = termo1 + termo2

print(f"{termo1} -> {termo2} -> ", end="")

contador = quantidade - 2
while contador > 0:
    termo3 = termo1 + termo2
    print(f"{termo3} -> ", end="")
    termo1 = termo2
    termo2 = termo3
    contador -= 1

print("FIM")
