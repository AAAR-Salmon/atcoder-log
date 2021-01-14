import sys
sys.setrecursionlimit(100000)

H,W=map(int,input().split())
done=[[False] * W for _ in range(H)]
c=[None]*H
x=y=0

ans = False

def dfs(x,y):
	global ans
	if ans:
		return
	if c[x][y] == 'g':
		ans = True
		return
	for (i,j) in [(x,y+1), (x+1,y), (x,y-1), (x-1,y)]:
		if 0 <= i < H and 0 <= j < W and not done[i][j] and c[i][j] != '#':
			done[i][j] = True
			dfs(i,j)

for i in range(H):
	c[i]=input()
	if 's' in c[i]:
		x=i
		y=c[i].index('s')
dfs(x,y)
print('Yes' if ans else 'No')
