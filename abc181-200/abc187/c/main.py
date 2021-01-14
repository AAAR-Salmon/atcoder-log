N = int(input())
S_noexc = []
S_exc = []
ans = 'satisfiable'
for i in range(N):
    s = input()
    if s[0] == '!':
        S_exc.append(s[1:])
    else:
        S_noexc.append(s)
S_exc.sort()
S_noexc.sort()
L = len(S_noexc)
if L == 0:
    print(ans)
    exit(0)
for t in S_exc:
    left = -1
    right = L
    while right - left > 1:
        mid = (left + right) // 2
        if S_noexc[mid] >= t:
            right = mid
        else:
            left = mid
    if right < L and S_noexc[right] == t:
        ans = t
        break
print(ans)