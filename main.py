import random

# Заповнення списку випадковими числами
random_numbers = [random.randint(-100, 100) for _ in range(10)]

# Виведення списку
print("Список випадкових чисел:", random_numbers)

# Cумма негативних чисел
negative = sum(x for x in random_numbers if x < 0)
print("Сума негативних чисел:", negative)

# Cумма парних чисел
even_num = sum(x for x in random_numbers if x % 2 == 0)
print("Сума парних чисел:", even_num)

# Cуми непарних чисел
sum_odd = sum(x for x in random_numbers if x % 2 != 0)
print("Сума непарних чисел:", sum_odd)



