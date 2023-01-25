arr = []
n = int(input("Введите количество элементов массива: "))
for i in range(n):
    arr.append(int(input("Введите элемент массива: ")))
    
sum_even = 0
prod_odd = 1
for i in range(len(arr)):
    if i % 2 == 0: # если четный индекс, то суммируем
        sum_even += arr[i]
    else: # если нечетный, то умножаем
        prod_odd *= arr[i]
        
print("Сумма элементов с чётным номерами:", sum_even)        
print("Произв. элементов с нечётным номерами:", prod_odd)