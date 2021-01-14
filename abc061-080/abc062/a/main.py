group = [-1] * 13
for i in [1,3,5,7,8,10,12]:
	group[i] = 0
for i in [4,6,9,11]:
	group[i] = 1
group[2] = 2

x,y = map(int,input().split())
print('Yes' if group[x] == group[y] else 'No')
