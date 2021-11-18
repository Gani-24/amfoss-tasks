import math
n=int(input())
s=0
for i in range(1,int(math.sqrt(n)+1)):
  if n%i==0 :
    if n/i==i:
      s+=1
    else:
      s+=2
print(s)