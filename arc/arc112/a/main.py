T = int(input())
for i in range(T):
	L,R = map(int,input().split())
	d = max(R - 2 * L + 1, 0)
	print(d * (d+1) // 2)
