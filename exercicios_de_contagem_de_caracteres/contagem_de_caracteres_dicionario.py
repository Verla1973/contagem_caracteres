def contar_caracteres(s):
    """Função que conta o número de caracteres de uma string
    Ex:
    >>> contar_caracteres('verla')
    a: 1
    e: 1
    l: 1
    r: 1
    v: 1

    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada
    """



    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


if __name__ == '__main__':
    str1 = str(input('Digite a string que você deseja fazer a contagem: '))
    print(contar_caracteres(str1))
    print()
    print(contar_caracteres('banana'))
