import xml.etree.ElementTree as ET
import json
import yaml

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
    