import re #regular Expressions
from collections import Counter

with open('test.txt') as f:
    text = f.read().lower()

words = re.findall(r'\w+', text)
print(Counter(words).most_common(1))