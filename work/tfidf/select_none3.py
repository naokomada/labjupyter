# -*- coding: utf-8 -*-
import MeCab
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

def printList(list):
    for st in list :
        print st


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    file = open(filename).read()
    feature_words = extractNoun(unicode(file, CharEncoding))
    data = []
    print(type(data))
    for x in feature_words:
        data.append(unicode(x, CharEncoding))

    vectorizer = TfidfVectorizer(lowercase=False, token_pattern=u'(?u)\\b\\w+\\b')
    tfidf = vectorizer.fit_transform(data)

    print printList(tfidf.toarray())
    #print printList(vectorizer.get_feature_names())
