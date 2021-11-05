usuario_saiu = False

while not usuario_saiu:
    valor1 = int(input("Primeiro valor: "))
    valor2 = int(input("Segundo valor: "))

    while True:
        print("""   O que você deseja?
        1 - Somar
        2 - Multiplicar
        3 - Maior
        4 - Novos números
        5 - Sair do programa    
        
        Digite a opção correspondente ao número: """)
        opcao = input(">>> ")

        if opcao == "1":
            soma = valor1 + valor2
            print(f"A soma entre {valor1} e {valor2} é igual a {soma}.")

        elif opcao == "2":
            produto = valor1 * valor2
            print(f"O produto entre {valor1} e {valor2} é igual a {produto}.")

        elif opcao == "3":
            if valor1 > valor2:
                maior = valor1
                print(f"Entre {valor1} e {valor2} o maior é {maior}.")
            elif valor1 == valor2:
                print(f"Valores iguais.")
            else:
                maior = valor2
                print(f"entre {valor1} e {valor2} o maior é {maior}.")

        elif opcao == "4":
            print("Informe os números novamente!")
            break

        elif opcao == "5":
            usuario_saiu = True
            break

        else:
            print("Oops! Valor inválido! Digite novamente.")
