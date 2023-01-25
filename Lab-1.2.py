# Ввод массива чисел
arr = list(map(int, input('Введите числа через пробел: ').split()))

# Нахождение индексов минимального и максимального элементов
min_index = arr.index(min(arr))
max_index = arr.index(max(arr))

# Перестановка элементов
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print('Новый массив:', arr)