import numpy as np
import math

class Metadata:
	slang = set(["bruh", "bro", "ngl", "¯\_(ツ)_/¯"])
	features = {}

	def __init__(self, features=['vocab', 'upper']):
		self.freq = dict()
		self.features = features

	def transform(self, msgs):
		result = []
		for msg in msgs:
			vec = []
			for feature in self.features:
				vec.append(Metadata.features[feature](self, msg))
			result.append(vec)
		return np.array(result)

	def n_upper(self, msg):
		if len(msg) == 0:
			return 0
		return math.sqrt(sum([1 for c in msg if c.isupper()]) / sum([1 for c in msg if c != ' ']))

	def n_len(self, msg):
		return math.log(len(msg.split(" ")))

	def n_freq(self, msg):
		words = msg.lower().split(" ")
		return math.log(1+sum([{
			1: 1,
			2: 0.95,
			3: 0.9,
			4: 0.5,
			5: 0.3,
			6: 0.1
		}.get(self.freq.get(word, 0), 0) for word in words]))

	def fit(self, msgs, y, *args):
		for msg in msgs:
			msg = msg.lower()
			for word in msg.split(" "):
				self.freq[word] = self.freq.get(word, 0) + 1


		return self

Metadata.features = {
	'vocab': Metadata.n_freq,
	'upper': Metadata.n_upper,
	'len': Metadata.n_len
}
