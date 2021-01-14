from sys import exit
S=input()
for i,c in enumerate(S):
  if i % 2 == 0 and c == 'L':
    print('No')
    exit()
  elif i % 2 == 1 and c == 'R':
    print('No')
    exit()
print('Yes')
