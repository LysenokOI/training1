import chardet

def define_file_encoding(filepath):
    with open(filepath, 'rb') as raw_content:
        return chardet.detect(raw_content.read()).get('encoding')

def load_raw_content(filepath, encoding):
    with open(filepath, mode='r', encoding=encoding) as raw_content:
        return raw_content.read()


define_file_encoding('Ferris.txt')
load_raw_content('Ferris.txt', 'encoding')

for line in raw_content:
    print(line)
