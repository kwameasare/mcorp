from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()

import re
import gensim
from gensim import corpora


def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


mylines = []
filepath = './ready.rtf'
with open(filepath, encoding='utf-8' ) as fp: 
    lines = fp.readlines()
    
    for i in range(0, len(lines)):
        
            
        line = lines[i]
       
        mylines.append(line)
        
        
        
        
# print(mylines)

doc_clean = [clean(doc).split() for doc in mylines]

# print(doc_clean)

# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in doc_clean:
    for token in text:
        frequency[token] += 1


processed_corpus = [[token for token in text if frequency[token] > 1] for text in doc_clean]

#print(processed_corpus)
dictionary = corpora.Dictionary(processed_corpus)

#print(dictionary) #prints number of unique tokens
# print(dictionary.token2id)
# print('Number of doc frequency: ',dictionary.dfs)
# print('Number of docs: ',dictionary.num_docs)
# print('Number of nonzeroes: ', dictionary.num_nnz)
# print('Number of processed words: ', dictionary.num_pos )


corpus = [dictionary.doc2bow(text) for text in processed_corpus]


# with open('output.txt', 'w') as f : 
#     print(corpus, file = f)
#print(corpus)
mcorp= []
mcorp = corpus.copy()

print(mcorp)

#print(mcorp)

# for x in range(len(mcorp)): 
#         print(x)
for i in range(0,len(mcorp),2):
        arr = []
        title = mcorp[i]
        ttl = len(mcorp[i])

        acle = mcorp[i+1]
        acl = len(mcorp[i+1])
        
        
        
        koo = tuple(map(str, title))
        jck = ''.join(koo)

        tonto = re.sub(', ',':',jck)
        jz = tonto.replace("(","")
        byce = jz.replace(")"," ")
        # print(byce)

        #print(ttl,acl,title,acle)

        knta = tuple(map(str, acle))
        jck = ''.join(knta)

       

        tonta = re.sub(', ',':',jck)
        man = tonta.replace("(","")
        
        shta = man.replace(")"," ")
        print(shta)

        


               

       




        # jnd = byce + shta
        # print(jnd)

        
        
        with open('ready_output.txt', 'a+') as f : 
                f.write("%d,%d %s \r\n" %(ttl,acl,byce+shta))
                
                

# with open('output.txt', encoding='utf-8' ) as fp: 
#             lines = fp.readlines()
    
#             for i in range(0, len(lines)):
        
            
#                 line = lines[i]
       
#                 koo = re.sub(',',':',line)
#                 print(koo)     


        # print(ttl,acl,title,acle)

        


       



