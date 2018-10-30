import chardet
import re

def define_file_encoding(filepath):
    with open(filepath, 'rb') as raw_content:
        return chardet.detect(raw_content.read()).get('encoding')

def load_raw_content(filepath, encoding):
    with open(filepath, mode='r', encoding=encoding) as raw_content:
        return raw_content.read()

def word_catalg(lst):
    catalg = {}
    for itm in lst:
        if itm not in catalg:
            catalg[itm] = 1
        else:
            catalg[itm] += 1
    return(catalg)


def output_max(max_frq_word, word_frq_cat):
    for value in max_frq_word:
        if len(max_frq_word) > 1:
            print('Most common word', max_frq_word.index(value) + 1, ': ', value, ', Found in the text ', word_frq_cat[value], ' times')
        else:
            print('Most common word:', value, ', Found in the text ', word_frq_cat[value], ' times')


print('Input file name:')
text_file = input() + '.txt'
encod_file = define_file_encoding(text_file)
read_text = load_raw_content(text_file, encod_file)
reg_ex = re.compile("[\w']+")
list_text = reg_ex.findall(read_text)
# print(list_text)  если хочется посмотреть на список
word_freq_catalog = word_catalg(list_text)  # function for creating couples
max_freq_word = [key for key, val in word_freq_catalog.items() if val == max(word_freq_catalog.values())] # key
output_max(max_freq_word, word_freq_catalog)
