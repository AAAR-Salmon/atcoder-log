s = input()
t = input()
ss = s+s
ans = -1
for i in range(len(s)):
	if ss[len(s)-i:len(ss)-i] == t:
		ans = i
		break
print(ans)
