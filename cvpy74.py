from random import randint
sorteados = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print("Os valores sorteados foram: ", end="")
for valor in sorteados:
    print(f"{valor}", end=" ")

print(f"\nO maior valor sorteado foi {max(sorteados)}")
print(f"O menor valor sorteado foi {min(sorteados)}")