N=int(input())
s=input()
r=0
for c in s:
  if c == 'R':
    r += 1
print('Yes' if r * 2 > N else 'No')
