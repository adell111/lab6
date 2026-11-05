from collections import Counter

numbers = [1,2,3,4,5,1,5,67,3,5]
counts = Counter(numbers) # Возвращает словарь сколько раз встречается каждый эл. в списке
duplicates = []
for num,count in counts.items():
    if count > 1:
        duplicates.append(num)

print(f"Дубликаты: {duplicates}")