s = bytearray(input().encode())
K = int(input())

for i in range(len(s)):
	if K == 0:
		break
	if s[i] > 97 and K >= 123 - s[i]:
		K -= 123 - s[i]
		s[i] = 97

if K > 0:
	s[-1] = (s[-1] - 97 + K) % 26 + 97

print(s.decode())
