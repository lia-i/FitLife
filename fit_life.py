# Проект FitLife - MVP версия 1.0


class LogicalError(Exception):
    """Обрабатывает логические ошибки"""

    pass


WATER_PER_KG = 30
ML_FOR_L = 1000


def calculate_bmi(weight, height):
    """Возвращает ИМТ."""
    result = weight / (height ** 2)
    return result


def calculate_water(weight):
    """Возвращает небходимый объем воды."""
    result = round(weight * WATER_PER_KG / ML_FOR_L, 1)
    return result


# 1. Знакомство
# Спроси у пользователя имя и сохрани в переменную user_name
user_name = input("Введите свое имя: ")

# Спроси возраст и сохрани в переменную user_age

while True:
    try:
        user_age = int(input("Введите свой возраст в годах: "))

        if user_age <= 0:
            raise LogicalError("возраст должен быть больше 0")
        break
    except ValueError:
        print("Ошибка: нужно ввести целое число! Попробуйте ещё раз.")
    except LogicalError as e:
        print(f"Ошибка: {e}! Попробуйте ещё раз.")


# 2. Сбор данных
# Запроси вес (в кг) и сохрани в user_weight (тип float)

while True:
    try:
        user_weight = float(input("Введите свой вес в киллограмах,"
                                  " например, 108.5: "))

        if user_weight <= 0:
            raise LogicalError("вес должен быть больше 0")
        break
    except ValueError:
        print("Ошибка: нужно ввести дробное число число, "
              "используя точку как разделитель. Попробуйте ещё раз.")
    except LogicalError as e:
        print(f"Ошибка: {e}! Попробуйте ещё раз.")

# Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)

while True:
    try:
        user_height = float(input("Введите свой рост в метрах,"
                                  " например, 1.68: "))

        if user_height <= 0:
            raise LogicalError("рост должен быть больше 0")
        break
    except ValueError:
        print("Ошибка: нужно ввести дробное число число, "
              "используя точку как разделитель. Попробуйте ещё раз.")
    except LogicalError as e:
        print(f"Ошибка: {e}! Попробуйте ещё раз.")

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# Рассчитай bmi (Индекс массы тела)
bmi = calculate_bmi(user_weight, user_height)

# Подсчет воды: вес * 30 мл
# Рассчитай water_needed
water_needed = calculate_water(user_weight)


# 4. Вывод красивого результата
# Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
print(" ")
print(f"Привет, {user_name}!")
# Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.

print(f"Возраст: {user_age}.")
print(f"Твой Индекс Массы Тела: {bmi:.1f}.")
print(f"Рекомендуемая норма воды: {water_needed} л. в день.")
print("Расчет окончен. Будьте здоровы!")
