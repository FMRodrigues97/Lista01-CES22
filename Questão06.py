import math
import sys


def is_prime(n):
    if n in (0, 1):
        print(f'O número {n} \033[1;31mNÃO\033[m é primo. ')
        return False
    if n < 0:
        print(f'Apenas números inteiros positivos não nulos podem ser primos')
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                print(f'O número {n} \033[1;31mNÃO\033[m é primo. ')
                return False
        print(f'O número é {n} \033[1;32mSIM\033[m primo. ')
        return True


def test(passou):
    linha = sys._getframe(1).f_lineno
    if passou:
        msg = f'Teste na linha {linha} \033[1;32mOK\033[m.'
    else:
        msg = f'Teste na linha {linha} \033[1;31mFALHOU\033[m.'
    print(msg)
    print()


def test_suite():
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19970109))
    test(is_prime(1))
    test(not is_prime(0))
    test(not is_prime(2017))
    test(not is_prime(2022))
    test(is_prime(20147))
    test(is_prime(2))
    test(is_prime(10))
    test(not is_prime(-10))
    test(is_prime(-1000))


test_suite()
