import time
from contextlib import contextmanager

@contextmanager
def timer():
	t = time.time()
	yield t
	print('This took {:f} seconds.'.format(time.time() - t))



with timer() as t:
	for i in range(100000):
		print(i**10)
	print('This code started at Unix time', t)