import re

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