import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()

import re
import gensim
from gensim import corpora


def w2v(fpath):


        def clean(doc):
                stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
                punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
                normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
                return normalized


        ttlines = []
        doclines=[]
        filepath = fpath
        with open(filepath, encoding='utf-8' ) as fp: 
                lines = fp.readlines()
        
        for i in range(0, len(lines),2):
                
                
                ttline = lines[i]
        
                ttlines.append(ttline)

        for c in range(1, len(lines),2):

                Docline=lines[c]

                doclines.append(Docline)


                
                
                
                
        # print(mylines)

        tt_clean = [clean(doc).split() for doc in ttlines]
        doc_clean = [clean(doc).split() for doc in doclines]


        # print(doc_clean)
        # print(tt_clean)


        # Count word frequencies
        from collections import defaultdict
        frequency = defaultdict(int)
        for text in doc_clean:
                for token in text:
                        frequency[token] += 1


        doc_corpus = [[token for token in text if frequency[token] > 1] for text in doc_clean]

        for titext in tt_clean:
                for tok in titext:
                        frequency[tok] += 1

        tt_corpus = [[tok for tok in titext if frequency[tok] > 1] for titext in tt_clean]
       
        # print(tt_corpus)

        ttdict = corpora.Dictionary(tt_corpus)
        with open('title_vocab.txt', '+w') as f : 
                        f.write(str(ttdict.token2id))

        docdict = corpora.Dictionary(doc_corpus)
        with open('doc_vocab.txt', '+w') as f : 
                        f.write(str(docdict.token2id))




        # print(dictionary) #prints number of unique tokens
        # print(ttdict.token2id)
        #print(docdict.token2id)
        # print('Number of doc frequency: ',dictionary.dfs)
        # print('Number of docs: ',dictionary.num_docs)
        # print('Number of nonzeroes: ', dictionary.num_nnz)
        # print('Number of processed words: ', dictionary.num_pos )


        


        dcorpus = [docdict.doc2bow(text) for text in doc_corpus]
        tcorpus=  [ttdict.doc2bow(titext) for titext in tt_corpus]

        # with open('output.txt', 'w') as f : 
        #     print(corpus, file = f)
        #print(corpus)
        doccorp= []
        doccorp = dcorpus.copy()

        ttcorp= []
        ttcorp = tcorpus.copy()

        # print(doccorp)

        # print(ttcorp)

        # for x in range(len(mcorp)): 
        #         print(x)
        for i in range(0,len(ttcorp)):
                arr = []
                title = ttcorp[i]
                ttl = len(ttcorp[i])

                acle = doccorp[i]
                acl = len(doccorp[i])
                
                
                
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
                #print(shta)

                


                

        




                # jnd = byce + shta
                # print(jnd)

                
                
                with open('cnbc_out.txt', 'a+') as f : 
                        f.write("%d,%d %s \r\n" %(ttl,acl,byce+shta))
                        
                

        # with open('output.txt', encoding='utf-8' ) as fp: 
        #             lines = fp.readlines()
        
        #             for i in range(0, len(lines)):
                
                
        #                 line = lines[i]
        
        #                 koo = re.sub(',',':',line)
        #                 print(koo)     


                # print(ttl,acl,title,acle)

                


w2v('./ready.rtf')



