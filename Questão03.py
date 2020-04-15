def sum_to(n):
    soma = 0
    for i in range(n, 0, -1):
        soma += i
    return soma


print(sum_to(10))
