# Link 1 = Q 12 - Programa para obter uma única string de duas strings fornecidas, separadas por um espaço e trocar os dois primeiros caracteres de cada string.


def juntarCaracteres(a, b):
    novoA = b[:2] + a[2:]
    novoB = a[:2] + b[2:]

    return novoA + '' + novoB
print(juntarCaracteres('abc', 'xyz'))