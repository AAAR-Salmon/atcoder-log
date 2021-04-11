import re

N = re.sub(r'0*$', '', input())
print('Yes' if all(N[i] == N[-i-1] for i in range(len(N) // 2)) else 'No')
