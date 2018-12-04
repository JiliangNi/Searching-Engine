from bs4 import BeautifulSoup
from collections import defaultdict
import re, os, time
import json
from math import log



##NUM_FOLDERS = 75
##NUM_FILES = 500
##
##index_dict = {}
##doc_count = 0
##
##def get_tokens(te):
##    return re.split("[^a-z0-9]+", te.lower())
##


with open('WEBPAGES_RAW/12/31', 'r') as f:
    sp = BeautifulSoup(f.read(), "lxml")
    for s in sp(["script", "style"]):
        #eliminate all content in <style> and <script> tag
        s.decompose()
    title_ls = []
    title = sp.title
    if title != None:
        temp_ls = get_tokens(sp.title.get_text())
        for item in temp_ls:
            title_ls.append(item.strip().encode("ascii","ignore"))

            
##
##
##    
##    text = sp.get_text()
##    
##    tokens = get_tokens(text)
##    
##    filename = '12/31'
##    
##    for item in tokens:
##        item = item.strip().encode("ascii","ignore")
##
##        if(index_dict.has_key(item)):
##            if index_dict[item].has_key(filename):
##                index_dict[item][filename] +=1
##            else:
##                index_dict[item][filename] = 1
##        else:
##            index_dict[item] = {filename:1}
##    # See title words as 10 copies
##    if title != None: 
##        for title_element in title_ls:
##            if title_element != '':
##                if not index_dict.has_key(title_element):
##                    index_dict[title_element] = {filename:10}
##                else:
##                    if index_dict[title_element].has_key(filename):
##                        index_dict[title_element][filename] += 9
##                    else:
##                        index_dict[title_element][filename] = 10

            
                



with open('output_new_Yang.json', 'r') as f:
    dt = json.loads(f.read())
    

f.close()
