from sys import exit
M,D=map(int,input().split())
cnt=0
if M < 4 or D < 22:
  print(0)
  exit()
for m in range(4,M+1):
  for d in range(22,D+1):
    if d % 10 >= 2:
      if m == (d//10)*(d%10):
        cnt += 1
print(cnt)
