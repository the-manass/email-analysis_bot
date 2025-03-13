import json
import yaml
import xml.etree.ElementTree as ET


# Функция проверки файла
def check_file(file_content, file_type):
    try:
        if file_type == "json":
            json.loads(file_content)  # Проверяем, можно ли распарсить JSON
            return "File is valid JSON!"

        elif file_type == "xml":
            ET.fromstring(file_content)  # Проверяем, можно ли распарсить XML
            return "File is valid XML!"

        elif file_type == "yaml":
            yaml.safe_load(file_content)  # Проверяем, можно ли распарсить YAML
            return "File is valid YAML!"

        else:
            return "Unsupported file type!"
    except Exception as e:
        return f"Invalid {file_type}: {e}"


# Тест проверок
if __name__ == "__main__":
    yaml_content = """
    name: John Doe
    age: 30
    hobbies:
      - Reading
      - Cycling
    """
    print(check_file(yaml_content, "yaml"))  # Output: File is valid YAML!
