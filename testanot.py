from typing import List, Tuple

# Тестовые данные.
TEST_DATA: List[Tuple[int, str, bool]] = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    """
    Увеличивает репутацию персонажа.

    :param current_rep: Текущая репутация.
    :param rep_points: Очки репутации для добавления.
    :param buf_effect: Флаг, указывающий на наличие буфера
    :return: Новое значение репутации с учетом эффекта.
    """
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


def remove_rep(current_rep: float, rep_points: int,
               debuf_effect: bool) -> float:
    """
    Уменьшает репутацию персонажа.

    :param current_rep: Текущая репутация.
    :param rep_points: Очки репутации для вычитания.
    :param debuf_effect: Флаг, указывающий на наличие дебаффа
    :return: Новое значение репутации с учетом эффекта.
    """
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep


def main(duel_res: List[Tuple[int, str, bool]]) -> str:
    """
    Основная функция для подсчета репутации персонажа.

    :param duel_res: Список кортежей с данными поединков
    :return: Строка с итоговым сообщением о репутации персонажа.
    """
    current_rep: float = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        elif result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return (f'После {len(duel_res)} поединков, '
            f'репутация персонажа — {current_rep:.3f} очков.')


# Тестовый вызов функции main.
print(main(TEST_DATA))
