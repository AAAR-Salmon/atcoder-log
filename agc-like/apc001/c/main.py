from functools import partial
print = partial(print, flush=True)

N = int(input())

l = 0
r = N

print(0)
sl = sr = input()
if sl == 'Vacant':
	exit(0)
while True:
	i = (l + r) // 2
	print(i)
	si = input()
	if si == 'Vacant':
		exit(0)
	if (si != sl) != ((i - l) % 2 == 0):
		l, sl = i, si
	else:
		r, sr = i, si
