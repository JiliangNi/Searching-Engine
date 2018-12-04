from bs4 import BeautifulSoup
from collections import defaultdict
import re, os, time
import json
from math import log

start = time.clock()

NUM_FOLDERS = 75
NUM_FILES = 500

index_dict = {}
doc_count = 0

def get_tokens(te):
    return re.split("[^a-z0-9]+", te.lower())


for i in range(0, NUM_FOLDERS):
    if i == NUM_FOLDERS - 1:
        NUM_FILES = 497
    for j in range(0, NUM_FILES):
        try:
            with open('WEBPAGES_RAW/' + str(i) + '/' + str(j) + '', 'r') as f:
                sp = BeautifulSoup(f.read(), "lxml")
                for s in sp(["script", "style"]):
                    #eliminate all content in <style> and <script> tag
                    s.decompose()

                # add more weight for words in title
##                title_ls = []
##                title = sp.title
##                if title != None:
##                    temp_ls = get_tokens(sp.title.get_text())
##                    for item in temp_ls:
##                        title_ls.append(item.strip().encode("ascii","ignore"))


                
                text = sp.get_text()
                tokens = get_tokens(text)
                
                filename = str(i) + "/" + str(j)
                
                for item in tokens:
                    item = item.strip().encode("ascii","ignore")

                    if(index_dict.has_key(item)):
                        if index_dict[item].has_key(filename):
                            index_dict[item][filename] +=1
                        else:
                            index_dict[item][filename] = 1
                    else:
                        index_dict[item] = {filename:1}
                # See title words as 3 copies
##                if title != None: 
##                    for title_element in title_ls:
##                        if title_element != '':
##                            if not index_dict.has_key(title_element):
##                                index_dict[title_element] = {filename:10}
##                            else:
##                                if index_dict[title_element].has_key(filename):
##                                    index_dict[title_element][filename] += 2
##                                else:
##                                    index_dict[title_element][filename] = 3
                    
                
            f.close()
            doc_count += 1
        except:
            print("Cannot open file", str(i) + "/" + str(j))

if index_dict.has_key(''):
    index_dict.pop('')
    
N = 37497
for term in index_dict:
    df = len(index_dict[term])
    idf = log(N/df)/log(10)
    for f in index_dict[term]:
        wtf = 1 + log(index_dict[term][f])/log(10) if index_dict[term][f] > 0 else 0
        index_dict[term][f] = wtf * idf

print ("total number of documents: ", doc_count)
print ("total number of unique tokens: ", len(index_dict))


with open('output_new.json', 'w') as index_file:
    json.dump(index_dict, index_file)

index_file.close()

    
        
print ("total time consume: ", time.clock() - start)
