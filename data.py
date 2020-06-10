import json
data = json.load(open("data.json"))

author_names = list(data.keys())

values = []
for author, messages in data.items():
	index = author_names.index(author)
	for msg in messages:
		values.append([msg, index])

import random
random.shuffle(values)

values_x = [i[0] for i in values]
values_y = [i[1] for i in values]

cutoff = int(len(values_x) * 2 / 3)
train_x = values_x[:cutoff]
train_y = values_y[:cutoff]
test_x = values_x[cutoff:]
test_y = values_y[cutoff:]

