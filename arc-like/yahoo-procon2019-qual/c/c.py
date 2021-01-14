K,A,B=map(int,input().split())
if B - A > 2:
	if 1 + K - 2 < A:
		print(1 + K)
	else:
		ans = A
		K -= A - 1
		if K % 2 == 1:
			ans += 1
			K -= 1
		ans += (B - A) * K // 2
		print(ans)
else:
	print(1 + K)
