from collections import deque
N,Q = map(int,input().split())
comp = [[None] * N for _ in range(N)]
ans = [i for i in range(N)]

def ntoa(n):
	return chr(ord('A')+n)

def compare(x,y):
	if comp[x][y] is not None:
		return comp[x][y]
	else:
		print(f'? {ntoa(x)} {ntoa(y)}', flush = True)
		R = input()
		comp[x][y] = R == '<'
		comp[y][x] = not comp[x][y]
		return comp[x][y]

def mergesort(arr, left, right, cmp):
	if right - left > 1:
		mid = (left + right) // 2
		mergesort(arr, left, mid, cmp)
		mergesort(arr, mid, right, cmp)
		merge(arr, left, mid, right, cmp)

def merge(arr, left, mid, right, cmp):
	L = deque(arr[left:mid])
	R = deque(arr[mid:right])
	for i in range(left, right):
		if not L:
			arr[i] = R.popleft()
		elif not R:
			arr[i] = L.popleft()
		elif cmp(R[0], L[0]):
			arr[i] = R.popleft()
		else:
			arr[i] = L.popleft()

mergesort(ans, 0, len(ans), compare)
print(f'! {"".join(map(ntoa, ans))}', flush = True)
