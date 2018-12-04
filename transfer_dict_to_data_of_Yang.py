from bs4 import BeautifulSoup
from collections import defaultdict
import re, os, time
import json
from math import log

NUM_FOLDERS = 75
NUM_FILES = 500

with open('output_new.json', 'r') as f:
    dt = json.loads(f.read())
f.close()

new_dt = {}

for term in dt:
    for filename in dt[term]:
        if not new_dt.has_key(filename):
            new_dt[filename] = {term:dt[term][filename]}
        else:
            new_dt[filename][term] = dt[term][filename]



with open('output_new_Yang.json', 'w') as index_file:
    json.dump(new_dt, index_file)

index_file.close()
