N,M,T = map(int,input().split())
bat = N
PA,PB = 0,0
ans = 'Yes'
for i in range(M):
	A,B = map(int,input().split())
	bat -= A - PB
	if bat <= 0:
		ans = 'No'
		break
	bat += B - A
	if bat > N:
		bat = N
	PA,PB = A,B
bat -= T - PB
if bat <= 0:
	print('No')
else:
	print(ans)
