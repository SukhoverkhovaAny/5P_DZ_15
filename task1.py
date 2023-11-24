# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os
import logging

PATH = 'example'
logger = logging.getLogger(__name__)
FORMAT = '{asctime:20} - {levelname:10} - "{name}" : {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='logging3.log', filemode='a',
                    level=logging.INFO)

def group_rename_file(path: str, end_name: str, original_ext: str, end_ext: str, len_num: int, range_start_name: int, range_end_name: int):
    serial_number = 0
    count = 0
    if serial_number < len_num: 
        files = os.listdir(path)
        for file_name in files:
            s = str(file_name).split('.')
            if s[-1] == original_ext:
                new_file_name = f'{file_name[range_start_name:range_end_name]}.{end_name}_{serial_number}.{end_ext}' 
                print(new_file_name) 
                os.rename(os.path.join(path,file_name), os.path.join(path,new_file_name))
                count += 1
            serial_number += 1
            logger.info(msg=f'Original file - {file_name}, renamed file - {new_file_name}')
        print(f'Групповое переименование завершено! Было переименовано {count} файлов')     

group_rename_file(PATH, end_name= 'rename', original_ext= 'doc', end_ext='exe', len_num = 50, range_start_name=3, range_end_name = 6)


