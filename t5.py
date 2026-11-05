list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

set1 = set(list1)
set2 = set(list2)

union = set1 | set2
inter = set1 & set2
razn = set1 - set2

print(f"Объединение: {sorted(union)}")
print(f"Пересечение: {sorted(inter)}")
print(f"Разность: {sorted(razn)}")
