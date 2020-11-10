from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize
import re
import string
from pathlib import Path
import ntpath


def transpose(m):
    col = len(m)
    row = len(m[0])
    new = [[0 for i in range (col)] for j in range (row)]
    for i in range (row):
        for j in range (col):
            new[i][j] = m[j][i]
    
    return new


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def takeCos(elem):
    return elem.get('cos')


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

    