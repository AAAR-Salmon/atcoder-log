N,K,X,Y = (int(input()) for _ in range(4))
ans = 0
if N <= K:
	ans = N * X
else:
	ans = K * X + (N-K) * Y
print(ans)
