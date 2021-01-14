N=int(input())
A=list(map(int,input().split()))
ans,m=0,0
for i in range(max(A), 1, -1):
	cnt=0
	for a in A:
		if a % i == 0:
			cnt += 1
	if cnt > m:
		m = cnt
		ans = i
print(ans)
