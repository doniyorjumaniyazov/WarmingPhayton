# # from pathlib import Path

# # print(Path.cwd())
# # #Path('directory').mkdir()
# # #Path('directory/').rmdir()
# # p = Path('directory')
# # #p.rename('sugar')
# # Path('directory').rename('sugar')

# import os  # Модуль для работы с файловой системой

# def bulk_rename_files(
#     target_name: str,  # Желаемое конечное имя файлов
#     digits: int,  # Количество цифр в порядковом номере
#     source_extension: str,  # Расширение исходных файлов, которые нужно переименовать
#     target_extension: str,  # Новое расширение для переименованных файлов
#     name_range: tuple[int, int],  # Диапазон сохраняемых символов из оригинального имени (start, end)
#     directory: str = "."  # Директория, где будут переименованы файлы (по умолчанию текущая)
# ):
#     """
#     Групповое переименование файлов в указанной директории.

#     :param target_name: Желаемое конечное имя файлов
#     :param digits: Количество цифр в порядковом номере
#     :param source_extension: Расширение исходных файлов
#     :param target_extension: Новое расширение для файлов
#     :param name_range: Диапазон символов из исходного имени для сохранения (start, end)
#     :param directory: Директория, в которой будут переименованы файлы (по умолчанию текущая)
#     """
#     # Проверяем, существует ли указанный каталог
#     if not os.path.exists(directory):
#         raise FileNotFoundError(f"Директория '{directory}' не найдена!")

#     # Получаем список всех файлов в указанной директории
#     files = os.listdir(directory)

#     # Фильтруем файлы по указанному расширению
#     source_files = [f for f in files if f.endswith(f".{source_extension}")]

#     # Проверяем, есть ли файлы для переименования
#     if not source_files:
#         print(f"Нет файлов с расширением '.{source_extension}' в директории '{directory}'.")
#         return

#     # Устанавливаем начальный счётчик для нумерации файлов
#     counter = 1

#     for file_name in source_files:
#         # Определяем путь к исходному файлу
#         source_path = os.path.join(directory, file_name)

#         # Извлекаем часть оригинального имени в заданном диапазоне
#         original_name_part = file_name[name_range[0]-1:name_range[1]]

#         # Создаём новое имя файла: сохраняем оригинальную часть, добавляем желаемое имя и номер
#         new_name = (
#             f"{original_name_part}_{target_name}_{str(counter).zfill(digits)}.{target_extension}"
#         )

#         # Определяем путь к новому файлу
#         target_path = os.path.join(directory, new_name)

#         # Переименовываем файл
#         os.rename(source_path, target_path)

#         # Увеличиваем счётчик
#         counter += 1

#     print(f"Успешно переименовано {counter - 1} файл(ов).")

