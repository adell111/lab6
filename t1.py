import random
from importlib.metadata import unique_everseen

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
unique_everseen()
print(f"Без дубликатов: {numbers.index(max(numbers))}")