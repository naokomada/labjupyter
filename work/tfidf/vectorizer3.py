

from sklearn.feature_extraction.text import TfidfVectorizer

data = ["Human machine interface for ABC computer applications",
            "A survey of user opinion of computer system response time",
            "The EPS user interface management system",
            "System and human system engineering testing of EPS",
            "Relation of user perceived response time to error measurement"]

vectorizer = TfidfVectorizer(lowercase=False, token_pattern=u'(?u)\\b\\w+\\b')
tfidf = vectorizer.fit_transform(data)

print tfidf.toarray()


print vectorizer.get_feature_names()
