print("    LOJA SUPER BARATÃO\n", "-" * 25)

custo_total = contador = mais_barato = 0
nome_mais_barato = ""

rodando = True
while rodando:
    nome = input("Nome do produto: ").strip().title()
    preco = float(input("Preço: R$"))
    custo_total += preco

    if custo_total == preco:
        mais_barato = preco
        nome_mais_barato = nome
    else:
        if preco < mais_barato:
            mais_barato = preco
            nome_mais_barato = nome
    if preco > 1000:
        contador += 1

    while True:
        resposta = input("Quer continuar? [S/N] ").strip().upper()
        if resposta == "S":
            break
        elif resposta == "N":
            rodando = False
            break

print(f"O total da compra foi R${custo_total:.2f}\nTemos {contador} produto(s) custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_mais_barato} que custa R${mais_barato:.2f}")
