
import re
from collections import Counter

with open('myfile.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]

word_counts = Counter(cap_words)
top_ten = word_counts.most_common(10)
print(top_ten)

