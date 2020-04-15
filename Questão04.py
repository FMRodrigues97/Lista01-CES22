def soma_questao4(lista):
    soma = 0
    for i in lista:
        if i % 2 == 1:
            soma += i
        else:
            break
    return soma


# TESTES:
print(soma_questao4([1, 2, 3, 5, 2, 9]))  # S soma será interrompida no primeiro elemento par (não incluso)
print(soma_questao4([1, 3, 9, 5]))  # Se não houver número par na lista, a soma incluirá todos os elementos da lista.
print(soma_questao4([]))  # Se não houverem elementos na lista, a soma dará zero.
print(soma_questao4([2, 5, 3, 5, 9, 1, 0]))  # Se o primeiro elemento já for par, a soma dará zero.
