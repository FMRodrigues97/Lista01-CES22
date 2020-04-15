print('\t', end='')
for i in range(1, 13):
    print(f'{i:5}', end='')
print()
print('   :'+'-' * 60)

for i in range(1, 13):
    print(f'{i:3}:', end='')
    for j in range(1, 13):
        print(f'{j * i:5}', end='')
    print()
print()