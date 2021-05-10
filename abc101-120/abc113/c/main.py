from heapq import heapify, heappush, heappop

N,M = map(int,input().split())
listPref = [[] for _ in range(N+1)]
for i in range(M):
	P,Y = map(int,input().split())
	heappush(listPref[P], (Y, i))
ids = [None] * M
for pref in range(1, N+1):
	x = 1
	prefStr = str(pref).zfill(6)
	while listPref[pref]:
		city = heappop(listPref[pref])[1]
		ids[city] = prefStr + str(x).zfill(6)
		x += 1
for id in ids:
	print(id, flush=False)
