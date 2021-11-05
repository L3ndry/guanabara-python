preco_compra = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
1 - à vista dinheiro/cheque
2 = à vista cartão
3 - 2x no cartão
4 - 3x ou mais no cartão
Qual é a opçâo? Digite abaixo!""")
resposta = int(input(">>> "))

if resposta == 1:
    desconto_10 = preco_compra - (preco_compra * 0.1)
    print(f"A sua compra de R${preco_compra:.2f} vai custar R${desconto_10:.2f} no final.")

elif resposta == 2:
    desconto_5 = preco_compra - (preco_compra * 0.05)
    print(f"A sua compra de R%{preco_compra:.2f} vai custar R${desconto_5:.2f} no final.")

elif resposta == 3:
    print(f"A sua compra de R${preco_compra:.2f} continuará com o mesmo preço no final.")

elif resposta == 4:
    parcelas = int(input("Quantas parcelas? "))
    preco_com_juros = preco_compra + (preco_compra * 0.2)
    preco_parcelado = preco_com_juros / parcelas
    print(f"A sua compra parecelada em {parcelas}x de R${preco_parcelado:.2f} COM JUROS")
    print(f"Sua compra de R${preco_compra:.2f} vai custar R${preco_com_juros:.2f} no final.")
