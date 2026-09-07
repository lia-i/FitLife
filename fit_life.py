
WATER_PER_KG = 30
ML_FOR_L = 1000


def calculate_bmi(weight, height):
    """Возвращает ИМТ."""
    return weight / (height ** 2)


def calculate_water(weight):
    """Возвращает небходимый объем воды."""
    return round(weight * WATER_PER_KG / ML_FOR_L, 1)


# запрашиваем имя, возраст, вес и рост
user_name = input("Введите свое имя: ")

# запрашиваем возраст, вес и рост
while True:
    try:
        user_age = int(input("Введите свой возраст в годах: "))
        break
    except ValueError:
        print("Ошибка: нужно ввести целое число!")

while True:
    try:
        user_weight = float(input("Введите свой вес в кг: "))
        break
    except ValueError:
        print(
            'Ошибка: нужно ввести дробное число. '
            'Используйте точку как разделитель. Попробуйте ещё раз.'
        )

while True:
    try:
        user_height = float(input("Введите свой рост в метрах: "))
        break
    except ValueError:
        print(
            'Ошибка: нужно ввести дробное число. '
            'Используйте точку как разделитель. Попробуйте ещё раз.'
        )

# рассчитываем индекс массы тела и необходимый объем воды
bmi = calculate_bmi(user_weight, user_height)
water_needed = calculate_water(user_weight)

# выводим отчет
print(
    f"\nПривет, {user_name}!"
    "\nВозраст: {user_age}."
    "\nВаш Индекс Массы Тела: {bmi:.1f}."
    "\nРекомендуемая норма воды: {water_needed} л. в день."
    "\nРасчет окончен. Будьте здоровы!",
)
