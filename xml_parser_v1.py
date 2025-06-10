import xml.etree.ElementTree as ET


def extract_wsdl_properties(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Put the namespace you want to 
        namespace = {'ns': 'http://www.somedomain.com/interface/v1_0'}

        # Find all item tags using the namespace
        items = root.findall('.//ns:item', namespaces=namespace)

        for item in items:
            # Get the name attribute of the item
            item_name = item.attrib.get('name', 'N/A')
            # Debugging: Print the item name
            print(f'Processing item: {item_name}')

            # Iterate through each property in the item
            for prop in item.findall('ns:property', namespaces=namespace):
                if prop.attrib.get('name') == 'wsdl':
                    wsdl_value = prop.attrib.get('value')
                    print(f'Item: {item_name}, WSDL: {wsdl_value}')
                    print('-' * 20)

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'your_file.xml' with the path to your WSDL
xml_file = 'your_file.xml'
extract_wsdl_properties(xml_file)
