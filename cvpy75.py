# 4 valores, qntd 9, posic 3, pares
numeros = (int(input("Digite um número: ")),
           int(input("Digite outro número: ")),
           int(input("Digite mais um número: ")),
           int(input("Digite o último número: ")))

print(f"O número '9' apareceu {numeros.count(9)} vez(es).")
if 3 in numeros:
    print(f"O número '3' está ta posição {numeros.index(3) + 1}")
print(f"Os números pares digitados:", end=" ")

for contador in numeros:
    if contador % 2 == 0:
        print(contador, end=" ")
