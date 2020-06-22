import data

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import FeatureUnion
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import numpy as np
import features

print("Logistic Regression")

clf = Pipeline([
	('input', FeatureUnion([
		('content', Pipeline([
			('count', CountVectorizer(lowercase=True)),
			('tfidf', TfidfTransformer())
		])),
		('metadata', features.Metadata(features=['upper']))
	])),
	('clf', LogisticRegression(max_iter=500))
])

clf.fit(data.train_x, data.train_y)
acc = np.mean(clf.predict(data.test_x) == data.test_y)
print ("acc=%f%%" % (acc*100))

while True:
	msg = input("> ")
	if msg == "":
		exit()
	index = clf.predict([msg])[0]
	print("'%s' => %s" % (msg, data.author_names[index]))

