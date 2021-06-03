dp = [0] * 19
for i in range(18):
	dp[i + 1] = 8 * dp[i] + 2 * 10**i


def f(n: int) -> int:
	p = len(str(n)) - 1
	top = n // 10**p
	rem = n % 10**p

	if n == 0:
		return 0

	if top < 4:
		return top * dp[p] + f(rem)
	elif top == 4:
		return top * dp[p] + rem + 1
	elif top < 9:
		return (top - 1) * dp[p] + 10**p + f(rem)
	else:
		return (top - 1) * dp[p] + 10**p + rem + 1


A, B = map(int, input().split())
print(f(B) - f(A - 1))
