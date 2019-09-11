#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

countDict = {}
current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            countDict[current_word] = current_count
        current_count = count
        current_word = word
if current_word == word:
    countDict[current_word] = current_count
countDict = sorted(countDict.items(), key=lambda kv: kv[1], reverse=True)
for i in countDict:
    print '%s\t%s' % (i[0], i[1])