import xml.etree.ElementTree as ET

def extract_wsdl_properties(xml_file, output_file='wsdl_output.txt'):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        namespace = {'ns': 'http://www.somedomain.com/interface/v1_0'}

        items = root.findall('.//ns:item', namespaces=namespace)

        with open(output_file, 'w') as f:
            for item in items:
                item_name = item.attrib.get('name', 'N/A')
                print(f'Processing item: {item_name}')
                f.write(f'Processing item: {item_name}\n')

                for prop in item.findall('ns:property', namespaces=namespace):
                    if prop.attrib.get('name') == 'wsdl':
                        wsdl_value = prop.attrib.get('value')
                        print(f'Item: {item_name}, WSDL: {wsdl_value}')
                        print('-' * 20)
                        f.write(f'Item: {item_name}, WSDL: {wsdl_value}\n')
                        f.write('-' * 20 + '\n')

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
xml_file = 'your_file.xml'
extract_wsdl_properties(xml_file)
