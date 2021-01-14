N = int(input())
T = list(map(int,input().split()))
M = int(input())
sumT = sum(T)
for i in range(M):
	P,X = map(int,input().split())
	print(sumT - T[P-1] + X)
