N,M,Q = map(int,input().split())
contestant_ac_list = [set() for _ in range(N+1)]
ac_contestant_num = [0] * (M+1)
for i in range(Q):
	s = list(map(int,input().split()))
	if s[0] == 1:
		print(sum(N - ac_contestant_num[i] for i in contestant_ac_list[s[1]]))
	else:
		ac_contestant_num[s[2]] += 1
		contestant_ac_list[s[1]].add(s[2])

