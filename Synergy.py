listOne = []
listTwo = []

print('Введите размер первого списка (до 100_000 чисел)')
lengthListOne = int(input('Длина первого списка = '))
if lengthListOne > 100_000:
    print('Превышено максимальное количество числел в писке 1')
else:
    for i in range(lengthListOne):
        listOne.append(input(f'Список 1 число №{i + 1} = '))

    print('Введите размер второго списка (до 100_000 чисел)')
    lengthListTwo = int(input('Длина второго списка = '))

    if lengthListTwo > 100_000:
        print('Превышено максимальное количество числел в писке 2')
    else:
        for i in range(lengthListTwo):
            listTwo.append(input(f'Список 2 число №{i + 1} = '))

        print(f'Общее колиичество чисел, которые содержать одновременно как в 1м так и во 2м списке = {len(set(listOne).intersection(set(listTwo)))}')

