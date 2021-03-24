N = 100000

isprime = [True] * (N + 1)
isprime[0] = isprime[1] = False
i = 2
while i ** 2 <= N:
	if isprime[i]:
		for j in range(i * 2, N + 1, i):
			isprime[j] = False
	i += 1

count_like_2017 = [0] * (N + 1)

for i in range(1, N + 1, 2):
	if isprime[i] and isprime[(i + 1) // 2]:
		count_like_2017[i] = 1

for i in range(1, N + 1):
	count_like_2017[i] += count_like_2017[i - 1]

Q = int(input())

for _ in range(Q):
	l, r = map(int,input().split())
	print(count_like_2017[r] - count_like_2017[l - 1])
