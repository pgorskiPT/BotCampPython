from zipfile import ZipFile
import xml.etree.ElementTree as ET
#from pydantic.v1 import root_validator

with ZipFile ("tabela_przestawna2.xlsx","r") as archive:
    with archive.open("xl/worksheets/sheet1.xml") as f:
        xml_content =f.read()

print(xml_content)

root=ET.fromstring(xml_content)
print(300*"=")

shared_strings = [elem.text for elem in root.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")]
print("Odczytane wartości tekstowe:", shared_strings)
print(300*"=")
# =======================================================
# otwieramy plik Excel jako zip
with ZipFile("tabela_przestawna21.xlsx", "r") as archive:
    print(archive)
    # with archive.open("xl/worksheets/sheet1.xml") as f:
    with archive.open("xl/sharedStrings.xml") as f:
        xml_content = f.read()

print(xml_content)

root = ET.fromstring(xml_content)

shared_strings = [elem.text for elem in root.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")]
print("Odczytane wartości tekstowe:", shared_strings)
print(150*"=")
# =======================================================
def convert_index_to_text(index):
    if index.isdigit():
        idx = int(index)
        if idx < len(shared_strings):
            return shared_strings[idx]
        else:
            return idx

with ZipFile("tabela_przestawna21.xlsx", "r") as archive:
    print(archive)
    with archive.open("xl/worksheets/sheet1.xml") as f:
    # with archive.open("xl/sharedStrings.xml") as f:
        xml_content = f.read()

print(xml_content)
print(150*"=")
sheet_root = ET.fromstring(xml_content)

# Przechodzimy przez wszystkie komórki i zamieniamy indeksy na tekst
data = []
for row in sheet_root.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row"):
    row_data = []
    for cell in row.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c"):
        cell_value = cell.find(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v")
        row_data.append(convert_index_to_text(cell_value.text) if cell_value is not None else "")
    data.append(row_data)
print(data)

import pandas as pd

df=pd.DataFrame(data)
print(df.head())
df.to_excel('fix2.xlsx',index=False)