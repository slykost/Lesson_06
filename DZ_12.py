#  ДЗ 12. Дан список из чисел и индекс элемента в списке k.

# Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент
# с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.

import random
lst = [random.randint(1, 50) for i in range(10)]
k = int(input('Введите число: '))               # индекс элемента
# print(lst) # можно просмотреть какое значение стоит под к сравнить исходное с выходящим
for i in range(k + 1, len(lst)):
        lst[i], lst[k] = lst[k], lst[i]
        k += 1
lst.pop()
print(lst)