N,M=map(int,input().split())
s=set(range(1,M+1))
for _ in range(N):
	A=set(map(int,input().split()[1:]))
	s = s & A
print(len(s))
