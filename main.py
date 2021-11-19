from pathlib import Path
import os

path = r"E:\new_papka"  # Путь к каталогу
text = "Timur"  # Текст для записи в начало файла
for filename in Path(path).rglob(f'*.txt'):  # Для всех файлов *.txt в каталоге (рекурсивно)
    try:
        lines = list()
        with open(os.path.join(path, filename), 'r') as f:
            for line in f.readlines():
                lines.append(line)
        print(f"Открыт файл {filename}")

        with open(os.path.join(os.getcwd(), filename), 'w') as f:
            f.write(text+'\n')
            for line in lines:
                f.write(line)
        print(f"Запись в файл успешна")
    except FileNotFoundError:
        print(f"Файл {filename} исчез во время исполнения")