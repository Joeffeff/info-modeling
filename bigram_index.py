import nltk
#nltk.download('punkt_tab') # Download the 'punkt' tokenizer
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
import re
from collections import Counter
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def search(query,bigram_list):
    q = query.lower().split()
    exists=[]
    if len(q)==1:
        for bigram, document in bigram_list.items():
            if q[0] in bigram:
                for d in document:
                    exists.append(d)
        print(set(exists))
    elif len(q)>1:
        q_bigram=list(bigrams(q))
        for qb in q_bigram:
            for bigram, document in bigram_list.items():
                if qb == bigram:
                    for d in document:
                        exists.append(d)
        results = Counter(exists)
        for r in results.keys():
            print(r, " : ", results[r])
        


docs = ["Silksong has been updated with a release year of 2025",
"Hollow Knight: Silksong Dev Breaks Silence Amidst Release Date Questions",
"'Silksong is real, progressing and will release', according to Team Cherry",
"I am done being excited about Hollow Knight: Silksong",
"'Hollow Knight: Silksong' Page Removed From Nintendo Store Has Returned",
"'Silksong' is definitely coming out this year",
"Silksong Officially Gets 2025 Release Date for Nintendo Switch 2"]

#normalization
for i in range(len(docs)):
    docs[i] = re.sub(r'[^\w\s]','',docs[i].lower())

tokens = []
for d in docs:
    t = word_tokenize(d)
    #removing stop words
    for word in t:
        if word in stop_words:
            t.remove(word)
    tokens.append(t)


bigram_list2 = []
for t in tokens:
    bigram_list2.append(list(bigrams(t)))

bigram_index={}

for bigram in bigram_list2:
    for b in bigram:
        documents=[]
        for i in range(7):
            if b in bigram_list2[i]:
                documents.append("Doc" +str(i+1))
        bigram_index[b] = documents


for bigram, document in bigram_index.items():
    print(bigram, document)

while (query := input("Enter a search query: ")) != "":
    search(query,bigram_index)
    pass