import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
 
np.set_printoptions(precision=2)
 
docs = np.array([
        'white black red',
        'white white black',
        'white black black black',
        'white'
        ])
 
vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')
vecs = vectorizer.fit_transform(docs)
 
print vecs.toarray()
