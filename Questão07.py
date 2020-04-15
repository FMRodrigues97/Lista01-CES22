import sys


def sum_of_squares(lista):
    quadrados = []
    for i in lista:
        quadrados.append(i**2)
    return sum(quadrados)


def test(passou):
    linha = sys._getframe(1).f_lineno
    if passou:
        msg = f'Teste na linha {linha} \033[1;32mOK\033[m.'
    else:
        msg = f'Teste na linha {linha} \033[1;31mFALHOU\033[m.'
    print(msg)
    print()


def test_suite():
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([2, -3, 4]) == 29)
    test(sum_of_squares([]) == 0)
    test(sum_of_squares([1, 2, 3]) == 10)
    test(sum_of_squares([1, 9, 9, 0]) == 163)


test_suite()
