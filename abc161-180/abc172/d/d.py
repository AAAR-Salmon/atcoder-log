N = int(input())
ans = 0
for j in range(1,N+1):
	ans += j * (N // j) * (N // j + 1) // 2
print(ans)
