#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
"""mapper.py"""

import sys

topWords = []
i=1
readConfigFile = open("nba_snewsData_wordcount.txt", "r") 
for readLine in readConfigFile: 
    words = readLine.split('\t', 1) 
    topWords.append(words[0]) 
    i+=1 
    if(i==11): 
        break

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for iw, w in enumerate(words):
        if w in topWords:
            for iu, u in enumerate(words):
                if (iw!=iu):
                    if u in topWords:
                        print '%s\t%s' % ("("+w+","+u+")", 1)
