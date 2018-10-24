import math

def sum(*args, **kwargs):
	s = 0
	print(args)
	print(kwargs)
	for x in args:
		s += x
	return s

print(sum(3,4,5))
print(sum(1,4,7,8,9,0,4,3,1,1, key1 = 'bla', key = math.pi))



# *[3, 4, 5] = 3, 4, 5
# **{'key1': 'bla', 'key2': math.pi} = key1 = 'bla', key2 = math.pi