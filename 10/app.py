import os
import shutil

# Пути к файлам
source_path = '/home/filedir/text.txt'  # Исходный файл (относительный путь)
destination_dir = '/home/otherfiledir/'  # Целевая директория
destination_path = os.path.join(destination_dir, 'text.txt')  # Полный путь к целевому файлу

# Создаем целевую директорию, если её нет
os.makedirs(destination_dir, exist_ok=True)

try:
    # Копируем содержимое файла
    shutil.copy2(source_path, destination_path)
    print(f"Файл успешно скопирован из {source_path} в {destination_path}")
except FileNotFoundError:
    print(f"Ошибка: исходный файл {source_path} не найден")
except PermissionError:
    print(f"Ошибка: нет прав на запись в {destination_dir}")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")