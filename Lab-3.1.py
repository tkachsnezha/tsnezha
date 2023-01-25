n = int(input('Введите размер матрицы: '))

a = [int(i) for i in input('Введите элементы верхнего треугольника: ').split()]

matrix = [[0] * n for i in range(n)]
k = 0
for i in range(n):
    for j in range(i + 1):
        matrix[i][j] = a[k]
        k += 1

        
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j] = matrix[j][i]

        
for row in matrix:  # построчно печатаем матрицу с помощью цикла for. 
    print(*row)
