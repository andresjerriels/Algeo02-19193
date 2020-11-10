from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize
import re
import string
from pathlib import Path
import ntpath


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def takeCos(elem):
    return elem.get('cos')

'''
def table_tf():
    step1_X = case_folding(X)
    stemmed_X = stemming(step1_X)
    tokenized_X = set(tokenize(stemmed_X))

    step1_Y = case_folding(Y)
    stemmed_Y = stemming(step1_Y)
    tokenized_Y = set(tokenize(stemmed_Y))
'''

def take1sentence(text):
    if len(text) > 100:
        text = text.partition('.')[0] + '.'
    return text


def tokenize(kalimat):
    return word_tokenize(kalimat)


def case_folding(kalimat):
    string_lower = kalimat.lower()
    numberless = re.sub(r"\d+", "", string_lower)
    no_punctuation = numberless.translate(str.maketrans("", "", string.punctuation))
    clean = no_punctuation.strip()
    return clean


def filtering(kalimat):
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()

    return stopword.remove(kalimat)


def stemming(kalimat):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    return stemmer.stem(kalimat)


def cosine_sim(rvector, tokenized_X, tokenized_Y):
    l1 = []
    l2 = []

    for word in rvector:
        count_x = sum(1 for words in tokenized_X if words == word)
        count_y = sum(1 for words in tokenized_Y if words == word)
        l1.append(count_x)
        l2.append(count_y)
        '''if word in tokenized_X:
            l1.append(1)
        else:
            l1.append(0)
        if word in tokenized_Y:
            l2.append(1)
        else:
            l2.append(0)'''

    cnt = 0
    for i in range(len(rvector)):
        cnt += l1[i] * l2[i]
        l1[i] = l1[i]**2
        l2[i] = l2[i]**2
    cosine = cnt / float((sum(l1) * sum(l2)) ** 0.5) #harusnya elementnya dikuadrat dulu ga si?

    lout = []
    for word in set(tokenized_X):
        count_Y_on_X = sum(1 for words in tokenized_Y if words == word)
        lout.append(count_Y_on_X)

    return cosine, lout
"""
X = input("Masukkan query: ")
doc = input("Masukkan nama file txt: ")

txt = Path(doc).read_text()
Y = txt.replace('\n', '')

step1_X = case_folding(X)
stemmed_X = stemming(step1_X)
tokenized_X = set(tokenize(stemmed_X))

step1_Y = case_folding(Y)
stemmed_Y = stemming(step1_Y)
tokenized_Y = set(tokenize(stemmed_Y))
tokenized_Ylist = tokenize(stemmed_Y)

rvector = tokenized_X.union(tokenized_Y)
l1 = []
l2 = []

wordDictA = dict.fromkeys(tokenized_X, 0)
for word in tokenized_Ylist:
    if word in wordDictA.keys():
        wordDictA[word] += 1

print(wordDictA)

for word in rvector:
    if word in tokenized_X:
        l1.append(1)
    else:
        l1.append(0)
    if word in tokenized_Y:
        l2.append(1)
    else:
        l2.append(0)

cnt = 0
for i in range(len(rvector)):
    cnt += l1[i] * l2[i]
cosine = cnt / float((sum(l1) * sum(l2)) ** 0.5)

print("Hasil cosine sim: " + str(cosine))
"""