import itertools

data = [.5, .7, 1, 7, 8]

groups = ['a', 'a', 'b', 'b', 'c']

for (g,d) in itertools.groupby(zip(groups,data), lambda x: x[0]):
	print(g,sum(list(zip(*d))[1]))