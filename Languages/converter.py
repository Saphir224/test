#To open and read the first Json English file 
import json
file_import = open('en.json', 'r' )
English_file_data = json.load(file_import)
file_import.close()

# To translate the values of keys in english
from deep_translator import GoogleTranslator
French_file_data ={}
for key in English_file_data:
    translated = GoogleTranslator(source='english', target='french').translate(English_file_data.get(key))
    French_file_data [key]= translated
#To Create a new json file 
with open("fr.json","w", encoding='utf-8') as dataCreate:
    json.dump(French_file_data, dataCreate, indent=3, ensure_ascii=False)

#To translate the values of keys in espagnol
Espagnol_data ={}
for key in English_file_data:
    translated = GoogleTranslator(source='english', target='spanish').translate(English_file_data.get(key))
    Espagnol_data[key]=translated
with open("es.json","w", encoding='utf-8') as dataCreate:
    json.dump(Espagnol_data, dataCreate, indent=3, ensure_ascii=False)