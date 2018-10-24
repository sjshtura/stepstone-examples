
def rev(lst):
    revl = []
    while lst:
        el = lst.pop()
        revl.append(el)
    return revl

def square(y):
	global x
	x = y**2

x = 4
square(10)
print(x)