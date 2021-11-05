valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

maior_valor = 0
menor_valor = 0
continua = True

if valor1 > valor2 and valor1 > valor3:
    maior_valor = valor1
    if valor2 > valor3:
        menor_valor = valor3
    else:
        menor_valor = valor2

else:
    if valor2 > valor3:
        maior_valor = valor2
        if valor1 > valor3:
            menor_valor = valor3
        else:
            menor_valor = valor1
    else:
        maior_valor = valor3
        if valor1 > valor2:
            menor_valor = valor2
        else:
            menor_valor = valor1

print(f"O maior valor digitado foi {maior_valor}.")
print(f"O menor valor digitado foi {menor_valor}.")

if continua:

    maior_valor = 0
    menor_valor = 0

    if valor1 > valor2 > valor3:
        maior_valor = valor1
        menor_valor = valor3
    elif valor1 > valor3 > valor2:
        maior_valor = valor1
        menor_valor = valor2
    elif valor2 > valor1 > valor3:
        maior_valor = valor2
        menor_valor = valor3
    elif valor2 > valor3 > valor1:
        maior_valor = valor2
        menor_valor = valor1
    elif valor3 > valor1 > valor2:
        maior_valor = valor3
        menor_valor = valor2
    elif valor3 > valor2 > valor1:
        maior_valor = valor3
        menor_valor = valor1

    print(maior_valor, menor_valor)
