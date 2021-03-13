N = int(input())
ans = 0
x = 1
p = 0
while N >= x * 1000:
	ans += x * 999 * p
	p += 1
	x *= 1000
ans += (N - x + 1) * p
print(ans)
