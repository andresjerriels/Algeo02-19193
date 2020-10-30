from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize
import re
import string


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


def cosine_sim(X, Y):
    step1_X = case_folding(X)
    stemmed_X = stemming(step1_X)
    tokenized_X = set(tokenize(stemmed_X))

    step1_Y = case_folding(Y)
    stemmed_Y = stemming(step1_Y)
    tokenized_Y = set(tokenize(stemmed_Y))

    rvector = tokenized_X.union(tokenized_Y)
    l1 = []
    l2 = []

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

    return cosine
