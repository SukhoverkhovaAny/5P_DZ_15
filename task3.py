# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

from random import randint
from sys import argv
import logging

logger = logging.getLogger(__name__)
FORMAT = '{asctime:20} - {levelname:10} - "{number}" : {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='logging1.log', filemode='a',
                    level=logging.INFO)


def random_num(upper_limit: int, lower_limit: int, attempts: int):
    number = randint(lower_limit, upper_limit)
    while attempts > 0:
        user_num = int(input(f'Введите число от {lower_limit} до {upper_limit} у вас есть {attempts} попыток: '))
        if user_num > number:
            print('Меньше')
        elif user_num < number:
            print('Больше')
        else:
            logger.info(msg=f'The number was guessed on the {attempts} try')
            return True
        attempts -= 1
    logger.info(msg=f'Attempts are exhaustes')
    return False





# print(random_num(100, 10, 10))


if __name__ == '__main__':
    options = tuple(map(int, argv[1:4]))
    lower_limit, upper_limit, attempts = 10, 100, 10
    match len(options):
        case 1:
            attempts = options[0]
        case 2:
            upper_limit, attempts = options
        case 3:
            ower_limit, upper_limit, attempts = options
    random_num(lower_limit, upper_limit, attempts)