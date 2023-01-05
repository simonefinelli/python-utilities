from lxml import etree
from datetime import datetime

current_date = datetime.now()

root = etree.Element("RootElement")
etree.SubElement(root, "SubElement1").text = 'place text'

se2 = etree.SubElement(root, "SubElement2")
etree.SubElement(se2, "SubSubElement").text = str(current_date)

 # Creating the XML file formatted
pprinted_xml = etree.tostring(root, encoding='UTF-8', xml_declaration=True, pretty_print=True)

path_to_save = './xml-file.xml'
with open(path_to_save, 'wb') as f:
    f.write(pprinted_xml)