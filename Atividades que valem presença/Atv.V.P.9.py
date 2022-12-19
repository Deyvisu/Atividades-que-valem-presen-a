#Link 1 = Q 15, Escreva um programa que pegue uma lista de palavras e retorne o tamanho da maior

def encontrarMaiorPalavra(listaPalavra):
    tamanhoPalavra = []

    for n in listaPalavra:
        tamanhoPalavra.append((len(n), n))
    tamanhoPalavra.sort()

    return tamanhoPalavra[-1][1]

print(encontrarMaiorPalavra(["Verde", "Azul", "Amarelo", "Vermelho"]))
