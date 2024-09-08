from math import sqrt

# Вывод приветственного сообщения.
message = (
    'Добро пожаловать в самую лучшую программу для вычисления '
    'квадратного корня из заданного числа'
)
print(message)


def calculate_square_root(number: float) -> float:
    """
    Вычисляет квадратный корень из заданного числа.

    :param number: Число, из которого вычисляется квадратный корень.
    :return: Квадратный корень числа.
    """
    return sqrt(number)


def calc(your_number: float) -> None:
    """
    Проверяет корректность числа и выводит его квадратный корень.

    :param your_number: Число, для которого нужно вычислить квадратный корень.
    """
    if your_number <= 0:
        print('Ошибка: число должно быть больше нуля.')
        return

    root = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {root:.2f}')


# Тестовый вызов функции calc.
calc(25.5)
