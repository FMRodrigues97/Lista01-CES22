import sys


def is_palindrome(frase_original):
    frase = frase_original.strip().lower()  # Lê a frase/palavra, elimina espaços antes e depois e deixa em minúsculas
    palavras = frase.split()  # Cria uma lista com as palavras da frase
    junto = ''.join(palavras)  # Une todas as palavras da frase eliminando os espaços
    inverso = junto[::-1]  # Cria o inverso da frase/palavra
    if inverso == junto:
        print(f'A frase/palavra "{frase_original.strip().upper()}" é \033[1;32mSIM\033[m um palíndromo')
        return True
    else:
        print(f'A frase/palavra "{frase_original.strip().upper()}" \033[1;31mNÃO\033[m é um palíndromo')
        return False


def test(passou):
    linha = sys._getframe(1).f_lineno
    if passou:
        msg = f'Teste na linha {linha} \033[1;32mOK\033[m.'
    else:
        msg = f'Teste na linha {linha} \033[1;31mFALHOU\033[m.'
    print(msg)
    print()


def test_suite():
    test(is_palindrome('abba'))
    test(not is_palindrome('abab'))
    test(is_palindrome('tenet'))
    test(not is_palindrome('banana'))
    test(is_palindrome('straw warts'))
    test(is_palindrome('a'))
    test(is_palindrome(''))
    test(is_palindrome('Socorram me subi no onibus em marrocos'))
    test(not is_palindrome('Arara'))


test_suite()
