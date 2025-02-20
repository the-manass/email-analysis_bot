import os

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