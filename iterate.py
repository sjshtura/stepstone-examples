import random
import itertools

li = [7,4,3,6,8,9]

def cumsum(li):
	s = 0
	for i in range(len(li)):
		s  += li[i]
		yield s

def listiter(li):
	for i in range(len(li)):
		yield li[i]

def dictiter10(d):
	for (key, value) in d.items():
		if value > 10:
			yield (key, value)

def randombits(p, nb_bits = 0):
	counter = 0
	while True:
		counter += 1
		if nb_bits > 0 and counter > nb_bits:
			break
		x = random.random()
		yield 1 if x < p else 0


for b in randombits(0.2, nb_bits = 100):
	print(b)
else:
	print('done iterating')







# for c in cumsum(li):
# 	print(c)

# mydict = {'a': 10, 'b': 9, 'c': 11}
# for (key, value) in dictiter10(mydict):
# 	print(key, value)

li=[-1,2,3,4,-1,1,1,-1,-1,-1,-1,-1,1]

for cat, sublist in itertools.groupby(li, lambda x: x>0):
	print(list(sublist))





