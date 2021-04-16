N,S=$<.read.split
T=S.clone
while T.include? p='()';T.gsub! p,'';end
puts'('*T.count(')')+S+')'*T.count('(')
