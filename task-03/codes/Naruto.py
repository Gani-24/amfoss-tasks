n=int(input())
a=list(map(int,input().strip().split()))
m=len(set(a))
r=max(a, key=a.count)
s=a.count(r)
print(s,m);