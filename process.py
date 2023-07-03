import json
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
similar=dict()
def filter_words(txt):
    words=[]
    for word in word_tokenize(txt):
        if word.isalpha():
            words.append(word)
    return words
def stemming(words):
    processed=[]
    stem = PorterStemmer()
    for word in words:
        processed.append(stem.stem(word))
    return processed
def removestopwords(words):
    removed=[]
    for word in words:
        if word not in stopwords.words('english'):
            removed.append(word)
    if len(removed)==0:
        return words
    else:
        return removed
def similarityfind(s1,s2,no):
    similars=s1.intersection(s2)
    similaritymeasure = len(similars)/(len(s1)+len(s2))
    if(similaritymeasure>=0.3):
        try:
            l=similar[similaritymeasure]
            similar[similaritymeasure].append(no)
        except:
            similar[similaritymeasure]=[no]
def getpattern():
    if len(similar)==0:
        return "I am Under Development Mode"
    else:
        count={}
        val=0
        for i in similar.keys():
            if(i>val):
                val=i
        for i in similar[val]:
            try:
                count[i]+=1
            except:
                count[i]=1
        index=-1
        max=0
        for i in count.keys():
            if(count[i]>max):
                index=i
                max=count[i]
        f = open('intent.json')
        data = json.load(f)
        return random.choice(data["intents"][index]["responses"])
def preprocess_text(request):
    request = filter_words(request)
    request = stemming(request)
    request = removestopwords(request)
    return request
def process_text(request):
    global similar
    similar={}
    request=preprocess_text(request)
    f = open('intent.json')
    data = json.load(f)
    i=0
    for elements in data['intents']:
        for pattern in elements['patterns']:
            pattern=preprocess_text(pattern)
            similarityfind(set(request),set(pattern),i)
        i+=1
    response=getpattern()
    return response.title()