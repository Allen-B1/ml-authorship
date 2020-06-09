import data

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np

clf = Pipeline([
    ('count', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])

clf.fit(data.train_x, data.train_y)
acc = np.mean(clf.predict(data.test_x) == data.test_y)

if __name__ == "__main__":
    print ("acc=%f%%" % (acc*100))
    print ("---")

    msgs = []
    while True:
        msg = input("")
        if msg == "":
            break
        msgs.append(msg)

    indexes = clf.predict(msgs)
    for msg, index in zip(msgs, indexes):
        print("'%s' => %s" % (msg, data.author_names[index]))
