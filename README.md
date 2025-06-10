# xml_parser (WSDL Property Extractor)

This simple Python script parses an XML or WSDL file and extracts specific `wsdl` property values from elements within a defined XML namespace. It is useful for inspecting service definitions, especially when dealing with custom WSDL interfaces.

## 🔧 Features

- Parses XML or WSDL files
- Extracts `wsdl` property values from `<item>` elements
- Handles XML namespaces
- Provides basic error handling

## 📂 Input

The script expects an XML file with the following structure (simplified):

```xml
<interface xmlns="http://www.somedomain.com/interface/v1_0">
    <item name="ExampleService">
        <property name="wsdl" value="http://example.com/service?wsdl"/>
    </item>
</interface>
```
_For example your_file.xml in this repository_

## 🚀 Usage
1. Make sure Python 3 is installed.
2. Replace the filename in the script:
```bash
xml_file = 'your_file.xml'
```
Run the script:
```bash
python extract_wsdl.py
```
## 📦 Dependencies
Uses only Python's built-in _xml.etree.ElementTree_ module (no external dependencies).

## 🛠 Configuration
If your XML uses a different namespace, edit this line:
```python
namespace = {'ns': 'http://www.somedomain.com/interface/v1_0'}
```
## 🧪 Example Output
Below data is printed in the output:

```
--------------
Processing item: ExampleService
Item: ExampleService, WSDL: http://example.com/service?wsdl
---------------
```
## 📄 License
MIT License

Feel free to fork or contribute!
