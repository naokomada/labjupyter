# -*- coding: utf-8 -*-

import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
 
CharEncoding = 'utf-8'

def extractNoun(text):
    """
       @input: sentence
       @return: a list of noun words
    """
    MecabMode = '-Ochasen'
    tagger = MeCab.Tagger(MecabMode)
    node = tagger.parseToNode(text.encode(CharEncoding))
    keywords = []
    while node:
        surface = node.surface.decode(CharEncoding)
        meta = node.feature.split(",")
        if meta[0] == '名詞':
            keywords.append(node.surface)
        node = node.next
    return keywords

def getSpacedNoneListFromFile(filename):
    file = open(filename).read()
    feature_words = extractNoun(unicode(file, CharEncoding))
    data = ''
    for x in feature_words:
        data += unicode(x, CharEncoding)
    return data

# python pp_class.py praporitext/sample1 praporitext/sample2 praporitext/othersample1 praporitext/othersample2 praporitext/othersample3

import sys
data1 = getSpacedNoneListFromFile('praporitext/sample1') # プライバシポリシー雛形
data2 = getSpacedNoneListFromFile('praporitext/sample2') # プライバシポリシー雛形
data3 = getSpacedNoneListFromFile('praporitext/sample3') # プライバシポリシー雛形
data4 = getSpacedNoneListFromFile('praporitext/sample4') # プライバシポリシー雛形
test1 = getSpacedNoneListFromFile('praporitext/sample5') # プライバシポリシー雛形
data100 = getSpacedNoneListFromFile('praporitext/othersample1') # wikipediaディズニーランド
data101 = getSpacedNoneListFromFile('praporitext/othersample2') # wikipedia仏教
data102 = getSpacedNoneListFromFile('praporitext/othersample3') # ジュゴン
test2 = getSpacedNoneListFromFile('praporitext/othersample3') # プラスチック
#testdata = sys.argv[0]
testdata = test2

#docs = np.array([data1,data2,data3,data4,data5,data6,testdata])
docs = np.array([data1,data2,data3,data100,data101, data102,testdata])

#
# ベクトル化
#
vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')
vecs = vectorizer.fit_transform(docs)
 
#print vecs.toarray()
 
#
# クラスタリング
#
clusters = KMeans(n_clusters=2, random_state=0).fit_predict(vecs)
print(type(clusters))
for doc, cls in zip(docs, clusters):
    #print cls, doc
    print cls
