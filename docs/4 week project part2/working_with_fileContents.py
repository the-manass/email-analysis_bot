import json
import yaml
import xml.etree.ElementTree as ET


def parse_file(file_content, file_type):
    if file_type == "json":
        return json.loads(file_content)  # Конвертация JSON в Python-словарь
    elif file_type == "xml":
        tree = ET.ElementTree(ET.fromstring(file_content))
        return xml_to_dict(tree.getroot())  # XML -> Словарь
    elif file_type == "yaml":
        return yaml.safe_load(file_content)  # Конвертация YAML в Python-объект
    else:
        return None


# Функция для XML -> Словарь
def xml_to_dict(element):
    result = {element.tag: {} if element.attrib else None}
    children = list(element)
    if children:
        dd = {}
        for child in children:
            dd.update(xml_to_dict(child))
        result[element.tag] = dd
    if element.attrib:
        result[element.tag].update(("@" + k, v) for k, v in element.attrib.items())
    if element.text:
        text = element.text.strip()
        if children or element.attrib:
            if text:
                result[element.tag]["#text"] = text
        else:
            result[element.tag] = text
    return result


# Тест конверсии
if __name__ == "__main__":
    xml_content = """<person><name>John Doe</name><age>30</age></person>"""
    parsed = parse_file(xml_content, "xml")
    print(parsed)  # Вывод: {'person': {'name': 'John Doe', 'age': '30'}}
