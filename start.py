import chardet
import re

def define_file_encoding(filepath):
    with open(filepath, 'rb') as raw_content:
        return chardet.detect(raw_content.read()).get('encoding')

def load_raw_content(filepath, encoding):
    with open(filepath, mode='r', encoding=encoding) as raw_content:
        return raw_content.read()


print('Input file name:')
text_file = input() + '.txt'
encod_file = define_file_encoding(text_file)
read_text = load_raw_content(text_file, encod_file)
reg_ex = re.compile("[\w']+")
list_text = reg_ex.findall(read_text)
print(list_text)
