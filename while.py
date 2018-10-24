
i = 0

while (i < 10):
	i += 1
	if (len(str(2**i))>10):
		print('number has become too long')
		break
	print(2**i)
else:
	print('all numbers were short enough')