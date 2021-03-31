N,M = map(int,input().split())
odd = even = 0
for i in range(N):
	if input().count('1') % 2 == 0:
		even += 1
	else:
		odd += 1
print(odd * even)
