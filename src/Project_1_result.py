import os
import re
import xml.etree.ElementTree as ET
import json
import yaml

# 1. Функция для определения типа файла
def detect_file_type(file_path):
    """Определяет тип файла по расширению."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    if ext == '.xml':
        return 'xml'
    elif ext == '.json':
        return 'json'
    elif ext in ('.yaml', '.yml'):
        return 'yaml'
    else:
        raise ValueError(f"Unsupported file type: {ext}")

# 2. Функция для анализа файла
def analyze_file(file_path, file_type):
    """Анализирует файл на предмет угроз."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Поиск URL-адресов
    urls = re.findall(r'https?://[^\s]+', content)
    if urls:
        print(f"Found URLs: {urls}")

    # Поиск base64-кодированных строк
    base64_pattern = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'
    base64_strings = re.findall(base64_pattern, content)
    if base64_strings:
        print(f"Found Base64 strings: {base64_strings}")

    # Поиск фишинговых ключевых слов
    phishing_keywords = ['password', 'login', 'account', 'verify', 'update', 'security']
    found_keywords = [word for word in phishing_keywords if word in content.lower()]
    if found_keywords:
        print(f"Found phishing keywords: {found_keywords}")

    return content

# 3. Функция для парсинга файла
def parse_file(content, file_type):
    """Парсит файл и возвращает краткое содержание."""
    if file_type == 'xml':
        root = ET.fromstring(content)
        summary = {elem.tag: elem.text for elem in root}
        return summary
    elif file_type == 'json':
        data = json.loads(content)
        summary = {key: str(value)[:50] for key, value in data.items()}  # Ограничиваем длину значения
        return summary
    elif file_type == 'yaml':
        data = yaml.safe_load(content)
        summary = {key: str(value)[:50] for key, value in data.items()}  # Ограничиваем длину значения
        return summary
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

# 4. Функция для сериализации данных
def serialize_data(data, output_format='json'):
    """Сериализует данные в указанный формат."""
    if output_format == 'json':
        return json.dumps(data, indent=4)
    elif output_format == 'yaml':
        return yaml.dump(data)
    elif output_format == 'xml':
        root = ET.Element('root')
        for key, value in data.items():
            elem = ET.SubElement(root, key)
            elem.text = str(value)
        return ET.tostring(root, encoding='unicode')
    else:
        raise ValueError(f"Unsupported output format: {output_format}")

# Основной скрипт
if __name__ == "__main__":
    # Укажите путь к файлу
    file_path = 'example.json'  # Замените на путь к вашему файлу

    # 1. Определяем тип файла
    file_type = detect_file_type(file_path)
    print(f"Detected file type: {file_type}")

    # 2. Анализируем файл на угрозы
    content = analyze_file(file_path, file_type)

    # 3. Парсим файл и получаем краткое содержание
    summary = parse_file(content, file_type)
    print("Summary of the file:")
    print(summary)

    # 4. Сериализуем данные в JSON (или другой формат)
    serialized_data = serialize_data(summary, output_format='json')
    print("Serialized data:")
    print(serialized_data)