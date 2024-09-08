from random import randint


def attack(char_name: str, char_class: str) -> str:
    """
    Рассчитывает и возвращает строку с описанием атаки персонажа.

    :param char_name: Имя персонажа.
    :param char_class: Класс персонажа ('warrior', 'mage', 'healer').
    :return: Описание нанесённого урона.
    """
    if char_class == 'warrior':
        damage = 5 + randint(3, 5)
        return f'{char_name} нанёс противнику урон, равный {damage}'
    if char_class == 'mage':
        damage = 5 + randint(5, 10)
        return f'{char_name} нанёс противнику урон, равный {damage}'
    if char_class == 'healer':
        damage = 5 + randint(-3, -1)
        return f'{char_name} нанёс противнику урон, равный {damage}'
    return f'{char_name} не смог нанести урон.'


def defence(char_name: str, char_class: str) -> str:
    """
    Рассчитывает и возвращает строку с описанием блока урона персонажем.

    :param char_name: Имя персонажа.
    :param char_class: Класс персонажа ('warrior', 'mage', 'healer').
    :return: Описание блокированного урона.
    """
    if char_class == 'warrior':
        block = 10 + randint(5, 10)
        return f'{char_name} блокировал {block} ед. урона'
    if char_class == 'mage':
        block = 10 + randint(-2, 2)
        return f'{char_name} блокировал {block} ед. урона'
    if char_class == 'healer':
        block = 10 + randint(2, 5)
        return f'{char_name} блокировал {block} ед. урона'
    return f'{char_name} не смог заблокировать урон.'


def special(char_name: str, char_class: str) -> str:
    """
    Возвращает строку с описанием применения специального умения персонажем.

    :param char_name: Имя персонажа.
    :param char_class: Класс персонажа ('warrior', 'mage', 'healer').
    :return: Описание применённого специального умения.
    """
    if char_class == 'warrior':
        ability = 80 + 25
        return (f'{char_name} применил специальное'
                f' умение «Выносливость {ability}»')
    if char_class == 'mage':
        ability = 5 + 40
        return (f'{char_name} применил специальное'
                f' умение «Атака {ability}»')
    if char_class == 'healer':
        ability = 10 + 30
        return (f'{char_name} применил специальное'
                f' умение «Защита {ability}»')
    return f'{char_name} не смог применить специальное умение.'


def start_training(char_name: str, char_class: str) -> str:
    """
    Начинает тренировку персонажа и управляет взаимодействием с пользователем.

    :param char_name: Имя персонажа.
    :param char_class: Класс персонажа ('warrior', 'mage', 'healer').
    :return: Сообщение о завершении тренировки.
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — великий мастер ближнего боя.')
    elif char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    elif char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')

    print('Потренируйся управлять своими навыками.')
    print(
        'Введи одну из команд: attack — чтобы атаковать противника, '
        'defence — чтобы блокировать атаку противника или '
        'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        elif cmd == 'defence':
            print(defence(char_name, char_class))
        elif cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """
    Управляет выбором класса персонажа.

    :return: Выбранный класс персонажа ('warrior', 'mage', 'healer').
    """
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ').lower()
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        elif char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        elif char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def main() -> None:
    """
    Основная функция, запускающая игру.

    Инициирует приветствие, ввод имени персонажа и его класса, а затем
    запускает тренировку.
    """
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
