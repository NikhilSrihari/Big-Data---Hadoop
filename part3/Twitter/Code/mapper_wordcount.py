#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
"""mapper.py"""

import sys

countDict = {}

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        if word in countDict:
            countDict[word]=countDict[word]+1
        else:
            countDict[word]=1
for countKey in countDict:
    print '%s\t%s' % (countKey, countDict[countKey])
