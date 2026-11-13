numbers = [1, 3, 5, 7, 9, 11, 13] # Наш лист
found = int(input("Введите искомое число: "))
left,right = 0, len(numbers) - 1 # Левая и правая границы
while left < right:
    mid = (left + right) // 2 # Находим середину
    if numbers[mid] == found:
        print(f"Ваше число стоит на позици {mid}")
        break
    elif numbers[mid] < found: # Если середина меньше искомого числа
        left = mid + 1 # Сдвигаем левую границу вправо
    else:
        right = mid # Иначе сдвигаем правую границу влево
else:
    print("Вашего числа нет в списке.")