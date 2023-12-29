# import random
#
# # Заповнення списку випадковими числами
# random_numbers = [random.randint(-100, 100) for _ in range(10)]
#
# # Виведення списку
# print("Список випадкових чисел:", random_numbers)
#
# # Cумма негативних чисел
# negative = sum(x for x in random_numbers if x < 0)
# print("Сума негативних чисел:", negative)
#
# # Cумма парних чисел
# even_num = sum(x for x in random_numbers if x % 2 == 0)
# print("Сума парних чисел:", even_num)
#
# # Cуми непарних чисел
# sum_odd = sum(x for x in random_numbers if x % 2 != 0)
# print("Сума непарних чисел:", sum_odd)
#
# # Добуток елементів з кратними індексами 3
# index_3 = 1
# for i in range(0, len(random_numbers), 3):
#     index_3 *= random_numbers[i]
# print("Добуток елементів з кратними індексами 3:", index_3)
#
# # Знаходження мінімального та максимального елементів
# min_value = min(random_numbers)
# max_value = max(random_numbers)
#
# # Добуток елементів між мінімальним та максимальним елементом
# min_index = random_numbers.index(min_value)
# max_index = random_numbers.index(max_value)
# min_and_max = 1
# for i in range(min(min_index, max_index) + 1, max(min_index, max_index)):
#     min_and_max *= random_numbers[i]
# print("Добуток елементів між мінімальним та максимальним елементом:", min_and_max)
#
# # Знаходження індексів першого та останнього позитивного елемента
# first_positive_index = next((i for i, x in enumerate(random_numbers) if x > 0), None)
# last_positive_index = next((i for i, x in enumerate(reversed(random_numbers)) if x > 0), None)
#
# # Обчислення суми елементів між першим та останнім позитивними елементами
# if first_positive_index is not None and last_positive_index is not None:
#     last_positive_index = len(random_numbers) - last_positive_index - 1
#     sum_between_positives = sum(random_numbers[first_positive_index + 1:last_positive_index])
#     print("Сума елементів між першим та останнім позитивними елементами:", sum_between_positives)
# else:
#     print("В списку немає позитивних елементів або їх замало.")
#
#
#

import random

# Заповнення списку випадковими числами
random_numbers = [random.randint(-100, 100) for _ in range(10)]

# Виведення списку
print("Список випадкових чисел:", random_numbers)

# Створення списку цілих, що містить лише парні числа
even_numbers = [x for x in random_numbers if x % 2 == 0]
print("Список парних чисел:", even_numbers)

# Створення списку цілих, що містить лише непарні числа
odd_numbers = [x for x in random_numbers if x % 2 != 0]
print("Список непарних чисел:", odd_numbers)

# Створення списку цілих, що містить лише негативні числа
negative_numbers = [x for x in random_numbers if x < 0]
print("Список негативних чисел:", negative_numbers)

# Створення списку цілих, що містить лише позитивні числа
positive_numbers = [x for x in random_numbers if x > 0]
print("Список позитивних чисел:", positive_numbers)