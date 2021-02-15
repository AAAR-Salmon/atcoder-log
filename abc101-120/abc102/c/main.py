N = int(input())
A = list(map(int,input().split()))
B = [A[i] - i - 1 for i in range(N)]
B.sort()
med = B[N // 2]
if N % 2 != 1:
	med = (med + B[N // 2 - 1]) // 2
	
print(min(sum(abs(B[i] - med) for i in range(N)),
          sum(abs(B[i] - med - 1) for i in range(N))))
