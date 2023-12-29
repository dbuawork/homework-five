import random

# Заповнення списку випадковими числами
random_numbers = [random.randint(-100, 100) for _ in range(10)]

# Виведення списку
print("Список випадкових чисел:", random_numbers)

# Cумма негативних чисел
negative = sum(x for x in random_numbers if x < 0)
print("Сума негативних чисел:", negative)

