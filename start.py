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
    return catalg

def getwordlist(raw_text):  # get list of separate words
    return_only_words = re.compile("[\w']+")
    only_words_list = return_only_words.findall(raw_text)
    return only_words_list


def output_max(max_frq_word, word_frq_cat):
    for value in max_frq_word:
        if len(max_frq_word) > 1:
            print('Most common word', max_frq_word.index(value) + 1, ': ', value, ', Found in the text ', word_frq_cat[value], ' times')
        else:
            print('Most common word:', value, ', Found in the text ', word_frq_cat[value], ' times')


def get_most_common_words(word_with_times_catalog):
    most_common_words = [key for key, val in word_with_times_catalog.items() if val == max(word_with_times_catalog.values())] # key
    return most_common_words

print('Input file name:')
text_file = input() + '.txt'
encod_file = define_file_encoding(text_file)
rawtext = load_raw_content(text_file, encod_file)
listed_text = getwordlist(rawtext)
# print(listed_text)  если хочется посмотреть на список
words_and_times_catalog = word_catalg(listed_text)  # function for creating couples
most_common_word = get_most_common_words(words_and_times_catalog)
output_max(most_common_word, words_and_times_catalog)
