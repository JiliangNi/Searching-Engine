from bs4 import BeautifulSoup
from collections import defaultdict
import re, os, time
import json
from math import log

with open('output.json', 'r') as f:
    index_dict = json.loads(f.read())
f.close()

N = 37497
index_dict.pop('')

for term in index_dict:

    df = len(index_dict[term])
    idf = log(N/df)/log(10)
    for f in index_dict[term]:
        wtf = 1 + log(index_dict[term][f])/log(10) if index_dict[term][f] > 0 else 0
        index_dict[term][f] = wtf * idf
        print(wtf * idf)
        print(term)
    
with open('output_new.json', 'w') as index_file:
    json.dump(index_dict, index_file)

index_file.close()
