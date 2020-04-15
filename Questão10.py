def soma_complexos(tupla1, tupla2):
    return f'({tupla1[0] + tupla2[0]})+({tupla1[1] + tupla2[1]})i'


tupla1 = (5, -2)
tupla2 = (-3, -1)
print(f'({tupla1[0]})+({tupla1[1]})i + ({tupla2[0]})+({tupla2[1]})i = {soma_complexos(tupla1, tupla2)}')
