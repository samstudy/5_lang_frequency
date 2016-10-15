import os
import re
import collections
from collections import Counter

quantity_words_to_show = 10

def load_data(filepath):
    if not os.path.exists(filepath):
       return None
    with open(filepath, 'r',encoding = 'utf-8') as file_handler:
       data = file_handler.read()
       return (data)

def get_most_frequent_words():
    action =  load_data(r'filepath')
    words = re.findall(r'\w+', action)
    resulting_count = collections.Counter(words)
    word_counts = Counter(resulting_count)
    top_ten = word_counts.most_common(quantity_words_to_show)
    return (top_ten)



if __name__ == '__main__':
    result = get_most_frequent_words()
    print (result)