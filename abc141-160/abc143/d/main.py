N = int(input())
L = list(map(int,input().split()))
L.sort()
ans=0
for i in range(N):
	for j in range(i+1,N):
		ok=j
		ng=N
		while ng - ok > 1:
			mid = (ok + ng) // 2
			if L[i] + L[j] > L[mid]:
				ok = mid
			else:
				ng = mid
		ans += ok - j
print(ans)
