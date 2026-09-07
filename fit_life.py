
WATER_PER_KG = 30
ML_FOR_L = 1000


class LogicalError(Exception):
    """Обрабатывает логические ошибки."""

    pass


def calculate_bmi(weight, height):
    """Возвращает ИМТ."""
    return weight / (height ** 2)


def calculate_water(weight):
    """Возвращает небходимый объем воды."""
    return round(weight * WATER_PER_KG / ML_FOR_L, 1)


def receive_data(name, data_type, description, err_text):
    """Обработка ошибок ввода параметров пользователя."""
    while True:
        value = input(f"Введите свой {name} {description}: ")
        try:
            if isinstance(value, data_type) and value <= 0:
                raise LogicalError("{name} должен быть больше 0")
            else:
                return type(value)
        except ValueError:
            print(err_text)
        except LogicalError as e:
            print(f"Ошибка: {e}! Попробуйте ещё раз.")


# запрашиваем имя
user_name = input("Введите свое имя: ")

# запрашиваем возраст, вес и рост
user_age = receive_data(
    'возраст',
    int,
    'в годах',
    'Ошибка: нужно ввести целое число. Попробуйте ещё раз.'
)

user_weight = receive_data(
    'вес',
    float,
    'в киллограмах, например, 108.5',
    'Ошибка: нужно ввести дробное число. '
    'Используйте точку как разделитель. Попробуйте ещё раз.'
)

user_height = receive_data(
    'рост',
    float,
    'в метрах, например, 1.77',
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
