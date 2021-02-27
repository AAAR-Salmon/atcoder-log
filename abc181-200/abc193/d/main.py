import sys
sys.setrecursionlimit(1000000)
import math
from math import sin, cos, tan, gcd
from functools import reduce
from collections import deque
from heapq import heapify, heappush, heappop
intm1 = lambda x:int(x)-1

K = int(input())
S = input()
T = input()
# tak_win[i][j]: 高橋、青木の残りの手札がi,jであるとき高橋が勝つかどうか
tak_win = [[False] * 10 for _ in range(10)]
tak_hand = [S.count(str(i)) for i in range(10)]
aok_hand = [T.count(str(i)) for i in range(10)]
for i in range(1, 10):
	for j in range(1, 10):
		tak_win[i][j] = sum(k * 10 ** (tak_hand[k] + (k == i)) for k in range(1, 10)) > sum(k * 10 ** (aok_hand[k] + (k == j)) for k in range(1, 10))

ans = 0
last = [K - tak_hand[i] - aok_hand[i] for i in range(10)]
for i in range(1, 10):
	for j in range(1, 10):
		if tak_win[i][j]:
			ans += last[i] * (last[j] - (i == j)) / (K * 9 - 8) / (K * 9 - 9)
print(ans)
