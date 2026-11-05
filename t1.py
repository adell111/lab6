import random
n = int(input('Ввеите число N: '))
numbers = [random.randint(1,100) for i in range(n)]
# Вывод нужных данных
print(f"Исходный список: {numbers}")
print(f"Сумма элементов: {sum(numbers)}")
print(f"Среднее: {sum(numbers)/n:.2f}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

# Сортировка
numbers.sort()
print(f"Отсортированный массив: {numbers}")
# Удаление дубликатов с сохранением порядка
print(f"Без дубликатов: {numbers.index(max(numbers))}")
print(f"Отсортированный массив: {sorted(numbers)}")
# Удаление дубликатов с сохранением порядка

unique = list(dict.fromkeys(numbers))
'''Создаем словарь, в котором ключами
будут элементы массива. Так как в python ключи не могут повторяться, то они будут уникальны'''
print(f"Без дубликатов: {unique}")
