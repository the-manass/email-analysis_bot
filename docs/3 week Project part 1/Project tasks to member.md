# 1-Developer 

Create a Parsing and Seriliazing functions to file
    1. parsing_file.py
    2. serilizing_file.py

# 2-Developer
    1. file_type.py
    2. analyse.document.py

    Как это работает:
detect_file_type: Определяет тип файла по расширению.

analyze_file: Анализирует содержимое файла на наличие угроз (URL-адреса, base64, фишинговые ключевые слова).

parse_file: Парсит файл и создает краткое содержание.

serialize_data: Сериализует данные в указанный формат (JSON, YAML, XML).



Пример вывода:
Для файла example.json с содержимым:

json

{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "s3cr3t"
}

    Вывод будет:

Detected file type: json
Found phishing keywords: ['password']
Summary of the file:
{'name': 'John Doe', 'email': 'john.doe@example.com', 'password': 's3cr3t'}
Serialized data:
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "s3cr3t"
}

Как адаптировать под другие форматы:
    Для XML-файла:

xml

<root>
    <name>John Doe</name>
    <email>john.doe@example.com</email>
    <password>s3cr3t</password>
</root>

    Для YAML-файла:


name: John Doe
email: john.doe@example.com
password: s3cr3t
Просто замените file_path на путь к вашему XML или YAML файлу, и код будет работать корректно.

Советы:
Если файл большой, используйте потоковую обработку (например, для JSON — ijson, для XML — xml.sax).

Добавьте обработку ошибок (например, если файл поврежден или имеет неверный формат).

Расширьте функционал, добавив поддержку других форматов (CSV, TXT и т.д.).
