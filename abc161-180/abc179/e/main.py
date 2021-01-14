N,X,M = map(int,input().split())
A = X
sumA = [0] * (M+1)
appeared = [-1] * M
appeared[X] = 0
for i in range(M):
	sumA[i+1] = sumA[i] + A
	A = A ** 2 % M
	if appeared[A] != -1:
		loopstart = appeared[A]
		loopend = i+1
		break
	else:
		appeared[A] = i+1
if N < loopend:
	print(sumA[N])
else:
	print(sumA[loopstart + (N - loopstart) % (loopend - loopstart)]
				+ (N - loopstart) // (loopend - loopstart)
				* (sumA[loopend] - sumA[loopstart]))
