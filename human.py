import data

for index, name in enumerate(data.author_names):
    print("%d (%s)" % (index, name))

print("\033[36m")
print("\033[1m=== GUESS ===\033[22m")

test_size = 16
correct = set()
for i in range(test_size):
    guess = input("'" + data.train_x[i] + "' => ")
    if guess == str(data.train_y[i]):
        correct.add(i)

print("\033[32m")
print("\033[1m=== ANSWERS ===\033[22m")

for i in range(test_size):
    print("[%s] %s' => %d (%s)" % ('C' if i in correct else 'W', data.train_x[i], data.train_y[i], data.author_names[data.train_y[i]]))

print("\033[33m")
print("\033[1m=== RESULTS ===\033[22m")

acc = len(correct) / test_size
print("acc=%f%%" % (acc * 100))