t,p=map(int,input().strip().split())
n=list(map(int,input().strip().split()))[:t]
m=list(map(int,input().strip().split()))[:p]
minimum_power=0
m.sort()
n.sort()
if(max(n)>max(m)):
    print("NO")
else:
    i=0
    j=0
    while i < len(n):
        if m[j] > n[i]:
            minimum_power+=m[j]
            i+=1
            j+=1
        else:
            j+=1
    if(i==len(n)):
       print("YES")
       print(minimum_power)


