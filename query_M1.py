from bs4 import BeautifulSoup
from collections import defaultdict
import re, os, time
import json


def get_file_path(query, postings):
    q = query.lower()
    if q in postings:
        return postings[q].keys()[:10]
    else:
        print("There is no such keyword!")

def get_path_url(ls, bk):
    result = []
    for item in ls:
        if item in bk:
            result.append((item, bk[item]))
    return result

with open('output2.txt', 'w+') as f3:

    with open('output.json', 'r') as f:
        index_dict = json.loads(f.read())
        file_ls = get_file_path('Informatics', index_dict)
        file_ls2 = get_file_path('Mondego', index_dict)
        file_ls3 = get_file_path('Irvine', index_dict)
        
        with open('WEBPAGES_RAW/bookkeeping.json', 'r') as f2:
            bk_dict = json.loads(f2.read())
            ls = get_path_url(file_ls, bk_dict)
            ls2 = get_path_url(file_ls2, bk_dict)
            ls3 = get_path_url(file_ls3, bk_dict)

        f3.write("1. Informatics\n\n")
        for i in range(0,10):
            f3.write(str(i+1) + ".\n\n")
            f3.write("DocID: " + ls[i][0] + "\n\n")
            f3.write("URL:\n")
            f3.write(ls[i][1])
            f3.write('\n\n')
        f3.write("\n\n2. Mondego\n\n")
        for i in range(0,10):
            f3.write(str(i+1) + ".\n\n")
            f3.write("DocID: " + ls2[i][0] + "\n\n")
            f3.write("URL:\n")
            f3.write(ls2[i][1])
            f3.write('\n\n')            
        f3.write("\n\n3. Irvine\n\n\n")
        for i in range(0,10):
            f3.write(str(i+1) + ".\n")
            f3.write("DocID: " + ls3[i][0] + "\n\n")
            f3.write("URL:\n")
            f3.write(ls3[i][1])
            f3.write('\n\n')

        f2.close()
    f.close()
f3.close()
