board = {}

for i in range(2):
	for j in range(2):
		board[(i,j)] = i*j

print(board)
del board[(2,2)]
print(board)