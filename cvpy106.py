def ajuda(comando):
    help(comando)


while True:
    print("\033[42m ", "- " * 14, "\033[m")
    print("\033[42m   Sistema de ajuda PyHelp!    \033[m")
    print("\033[42m", "- " * 14, " \033[m\n")
    resposta = str(input("Função ou Bibiolteca > ")).strip().upper()
    if resposta == "END":
        break
    else:
        print("\n\033[40m")
        ajuda(resposta.lower())
        print("\033[m")
