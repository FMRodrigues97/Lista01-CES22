def untill_sam(lista):
    contador = 0
    for i in lista:
        if i == 'sam':
            return contador+1
        else:
            contador += 1
    return contador


# TESTES:
print(untill_sam(['my', 'name', 'is', 'not', 'sam', 'wilson']))
print(untill_sam([]))  # Se não houver a palavra "sam" o resultado será o tamanho da lista
print(untill_sam(['essa', 'lista', 'não', 'vai', 'conter', 'a', 'palavra']))  # O resultado será o tamanho da lista
print(untill_sam(['sam', 'é', 'a', 'palavra', 'proibida']))  # Só será contabilizado o primeiro elemento da lista
print(untill_sam(['último', 'termo', 'é', 'sam']))  # Como a última palavra é "sam", o resultado será o tamanho da lista
