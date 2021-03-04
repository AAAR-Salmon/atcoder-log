N = int(input())
ans = 0
begin_b = end_a = both = 0
for _ in range(N):
	s = input()
	both += s[0] == 'B' and s[-1] == 'A'
	begin_b += s[0] == 'B' and s[-1] != 'A'
	end_a += s[0] != 'B' and s[-1] == 'A'
	for i in range(len(s) - 1):
		ans += s[i:i+2] == 'AB'
if begin_b == end_a == 0:
	print(ans + both - 1 + (both == 0))
else:
	print(ans + both + min(begin_b, end_a))
