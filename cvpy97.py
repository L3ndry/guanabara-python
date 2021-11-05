def escreva(palavra):
    tamanho = len(palavra) + 4
    print("-" * tamanho)
    print(f"  {palavra}")
    print("-" * tamanho)


while True:
    escrever = str(input("Escreva algo: (999 para sair) "))
    if escrever != "999":
        escreva(escrever)
    else:
        break
