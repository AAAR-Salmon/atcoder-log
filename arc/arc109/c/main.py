import math
from functools import reduce
from collections import deque
n,k=map(int,input().split())
s=input()

def game(left, right):
	if right - left > 1:
		mid = (left + right) // 2
		a = game(left, mid)
		b = game(mid, right)
		return win(a, b)
	else:
		return left

def win(a, b):
	A = s[a % n]
	B = s[b % n]
	if (A, B) in {('R', 'P'), ('P', 'S'), ('S', 'R')}:
		return b
	else:
		return a

print(s[game(0, 2**k) % n])
