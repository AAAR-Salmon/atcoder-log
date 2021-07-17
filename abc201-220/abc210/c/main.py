from collections import defaultdict


N, K = map(int, input().split())
C = list(map(int, input().split()))

ans = 0
candies = defaultdict(lambda:0)

for c in C[:K]:
	candies[c] += 1

ans = k = len(candies.keys())

for i in range(K, N):
	if candies[C[i]] == 0:
		k += 1
	candies[C[i]] += 1
	candies[C[i - K]] -= 1
	if candies[C[i - K]] == 0:
		k -= 1
	if k > ans:
		ans = k

print(ans)
