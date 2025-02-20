import xml.etree.ElementTree as ET
import json
import yaml



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
    