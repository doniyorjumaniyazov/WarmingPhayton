# №1 задания

#import logging

# # Создаем логгер для логирования сообщений
# logger = logging.getLogger('my_logger')

# # Устанавливаем минимальный уровень логирования для логгера. 
# # Этот уровень определяет, какие сообщения будут обрабатываться логгером.
# logger.setLevel(logging.DEBUG)  # Логгер будет обрабатывать все сообщения от DEBUG и выше

# # Создаем обработчик для записи сообщений уровня DEBUG и INFO в файл debug_info.log
# debug_info_handler = logging.FileHandler('debug_info.log')
# debug_info_handler.setLevel(logging.DEBUG)  # Этот обработчик будет обрабатывать сообщения от DEBUG и выше

# # Создаем обработчик для записи сообщений уровня WARNING и выше в файл warnings_errors.log
# warnings_errors_handler = logging.FileHandler('warnings_errors.log')
# warnings_errors_handler.setLevel(logging.WARNING)  # Этот обработчик будет обрабатывать сообщения от WARNING и выше

# # Создаем формат сообщений. В данном случае выводим время, уровень и само сообщение.
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# # Применяем форматтер к каждому обработчику
# debug_info_handler.setFormatter(formatter)
# warnings_errors_handler.setFormatter(formatter)

# # Добавляем обработчики к логгеру
# logger.addHandler(debug_info_handler)
# logger.addHandler(warnings_errors_handler)

# # Пример логирования сообщений разных уровней
# logger.debug("Это сообщение уровня DEBUG.")  # Это сообщение попадет в debug_info.log
# logger.info("Это сообщение уровня INFO.")  # Это сообщение попадет в debug_info.log
# logger.warning("Это сообщение уровня WARNING.")  # Это сообщение попадет в оба файла
# logger.error("Это сообщение уровня ERROR.")  # Это сообщение попадет в оба файла
# logger.critical("Это сообщение уровня CRITICAL.")  # Это сообщение попадет в оба файла

# №2 задания

#from datetime import datetime

# # Получаем текущее время и дату
# now = datetime.now()

# # Форматируем дату и время в нужный формат YYYY-MM-DD HH:MM:SS
# formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

# # Получаем день недели (0 - понедельник, 6 - воскресенье)
# day_of_week = now.strftime('%A')  # Название дня недели (например, Monday)

# # Получаем номер недели в году
# week_number = now.strftime('%U')  # Номер недели в году (начинается с воскресенья)

# # Выводим результаты
# print(f"Текущее время и дата: {formatted_datetime}")
# print(f"День недели: {day_of_week}")
# print(f"Номер недели в году: {week_number}")

# №3 задания

# from datetime import datetime, timedelta

# # Функция для вычисления даты через заданное количество дней
# def get_future_date(days: int):
#     # Получаем текущую дату и время
#     current_date = datetime.now()

#     # Создаем объект timedelta, который представляет собой интервал времени в днях
#     time_delta = timedelta(days=days)

#     # Рассчитываем дату, которая наступит через заданное количество дней
#     future_date = current_date + time_delta

#     # Преобразуем дату в строку в формате YYYY-MM-DD
#     formatted_future_date = future_date.strftime('%Y-%m-%d')

#     # Возвращаем отформатированную дату
#     return formatted_future_date

# # Пример вызова функции
# days = 10  # Количество дней от текущей даты
# future_date = get_future_date(days)
# print(f"Дата, которая наступит через {days} дня(ей): {future_date}")

# №4 задания

# import argparse

# # Создание парсера для обработки аргументов командной строки
# parser = argparse.ArgumentParser(description="Скрипт для работы с числом и строкой.")

# # Добавляем обязательные аргументы
# parser.add_argument('number', type=int, help="Число, которое нужно обработать.")
# parser.add_argument('text', type=str, help="Строка, с которой нужно работать.")

# # Добавляем необязательные флаги
# parser.add_argument('--verbose', action='store_true', help="Если установлен, выводит дополнительную информацию о процессе.")
# parser.add_argument('--repeat', type=int, default=1, help="Количество повторений строки. По умолчанию 1.")

# # Парсим аргументы
# args = parser.parse_args()

# # Выводим дополнительную информацию, если флаг --verbose установлен
# if args.verbose:
#     print(f"Запуск скрипта с параметрами: число={args.number}, строка='{args.text}', повторений={args.repeat}")

# # Выполняем повторение строки указанное количество раз
# output = args.text * args.repeat

# # Выводим результат
# print(f"Результат: {output}")

# # Если verbose включен, выводим дополнительную информацию
# if args.verbose:
#     print(f"Строка '{args.text}' повторена {args.repeat} раз.")

# №5 задания

import os
import logging
from collections import namedtuple
import argparse

# Определяем структуру для хранения информации о файле или каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_dir'])

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Функция для сбора информации о содержимом директории
def collect_directory_info(directory_path):
    # Получаем абсолютный путь к директории
    directory_path = os.path.abspath(directory_path)

    # Проверяем, существует ли указанный путь
    if not os.path.exists(directory_path):
        logging.error(f"Указанный путь не существует: {directory_path}")
        return

    # Проверяем, является ли это директорией
    if not os.path.isdir(directory_path):
        logging.error(f"Указанный путь не является директорией: {directory_path}")
        return

    # Проходим по содержимому директории
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)  # Получаем полный путь
        parent_dir = os.path.basename(directory_path)  # Название родительского каталога
        
        # Если это каталог, сохраняем информацию о нем
        if os.path.isdir(item_path):
            file_info = FileInfo(name=item, extension='', is_directory=True, parent_dir=parent_dir)
            logging.info(f"Каталог: {file_info}")
        # Если это файл, сохраняем информацию о файле
        elif os.path.isfile(item_path):
            name, extension = os.path.splitext(item)  # Разделяем имя и расширение
            file_info = FileInfo(name=name, extension=extension, is_directory=False, parent_dir=parent_dir)
            logging.info(f"Файл: {file_info}")

# Главная функция для парсинга аргументов и запуска сбора информации
def main():
    # Создаем парсер для командной строки
    parser = argparse.ArgumentParser(description="Скрипт для сбора информации о содержимом директории.")
    
    # Добавляем аргумент для пути до директории
    parser.add_argument('directory', type=str, help="Путь до директории, информацию о которой нужно собрать.")
    
    # Парсим аргументы командной строки
    args = parser.parse_args()

    # Собираем информацию о директори
    collect_directory_info(args.directory)

# Запуск программы
if __name__ == '__main__':
     main()
