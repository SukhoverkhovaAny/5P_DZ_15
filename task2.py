# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.
import logging


logger = logging.getLogger(__name__)
FORMAT = '{asctime:20} - {levelname:10} - "{name}" : {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='logging2.log', filemode='a',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
FORMAT = '{asctime:20} - {levelname:10} - "{name}" : {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='logging2.log', filemode='a',
                    level=logging.ERROR)

def get(dict_, key, value = None):
    try:
        logger.info(msg=f'Value - {dict_[key]}, by key- {key}')
        return dict_[key]
    except KeyError as exc:
        logger.error(msg=exc)


dct = {'one': 1, 'two': 2}
print(get(dct, 'tree', 3))

