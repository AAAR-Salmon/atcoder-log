N,X = map(int,input().split())
alc = 0
ans = -1
for i in range(N):
	V,P = map(int,input().split())
	alc += V * P
	if alc > X * 100:
		ans = i + 1
		break
print(ans)
