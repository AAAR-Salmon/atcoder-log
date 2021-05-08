MOD = 200

N = int(input())
A = list(map(lambda x: int(x) % MOD, input().split()))

ans = 0
for i in range(MOD):
	a = A.count(i)
	ans += a * (a - 1) // 2

print(ans)
