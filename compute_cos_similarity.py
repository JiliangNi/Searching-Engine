from bs4 import BeautifulSoup
from collections import defaultdict
import re, os, time
import json
from math import log
from math import sqrt

def get_tokens(te):
    return re.split("[^a-z0-9]+", te.lower())

with open('output_new_Yang.json', 'r') as f:
    dt = json.loads(f.read())
f.close()

with open('WEBPAGES_RAW/bookkeeping.json', 'r') as f2:
    bt = json.loads(f2.read())
f.close()


def get_idf(word,dt):
    count = 0
    for item in dt:
        if word in dt[item]:
            count += 1
    return count

def normalize(dt):
    temp_sum = 0
    for item in dt:
        temp_sum += dt[item] ** 2
    below = sqrt(temp_sum)
    result = {}
    for item in dt:
        result[item] = dt[item]/below
    return result
    
def get_cos_similarity(query,dt,bt):
    q_ls = []
    temp_ls = get_tokens(query)
    for item in temp_ls:
        q_ls.append(item.strip().encode("ascii","ignore"))
    q_dict = {}
    
    for item in q_ls:
        if q_dict.has_key(item):
            q_dict[item] += 1
        else:
            q_dict[item] = 1
    if q_dict.has_key(''):
        q_dict.pop('')
    

    doc_dt = {}
    for doc in dt:
        flag = True
        for item in q_dict:
            if item not in dt[doc]:
                flag = False
                break
        if flag == True:
            doc_dt[doc] = dt[doc]

    score_result = []
    
    for term in q_dict:
        wtf = 1 + log(q_dict[term])/log(10) if q_dict[term] > 0 else 0
        idf = get_idf(term,dt)
        w = wtf * idf
        q_dict[term] = w
    q_norm = normalize(q_dict)
    
    for item in doc_dt:
        doc_dt[item] = normalize(doc_dt[item])

    for item in doc_dt:
        score = 0
        for term in q_norm:
            score += q_norm[term] * doc_dt[item][term]

        score_result.append((item, score))
    score_result.sort(key = lambda x: -x[1])
    top_ten_ls = score_result[:10]
    urls = []
    for item in top_ten_ls:
        urls.append(bt[item[0]])
    for item in urls:
        print(item)
    return urls
    
