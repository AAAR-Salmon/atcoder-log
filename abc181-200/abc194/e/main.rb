N,M,*A=$<.read.split.map &:to_i
x=[0]*-~N
A[...M].each{|a|x[a]+=1}
m=x.index(0)
(0...N-M).each{|i|x[A[i+M]]+=1
if 0==x[A[i]]-=1 then;m=[m,A[i]].min;end}
p m
