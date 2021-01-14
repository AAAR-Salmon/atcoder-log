from functools import reduce
T=[0]*5
for i in range(5):
  T[i]=int(input())
T.sort(key=lambda x:(x+9)%10,reverse=True)
print(reduce(lambda x,y:x+(y+9)//10*10,T[:-1],0)+T[-1])
