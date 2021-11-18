n,m = map(int, input().split())
numbers = []
tempg=n
for boy in range(1,m+1):
    ans = -1
    tempb = boy
    n=tempg
    while(ans == -1):
        if(n % 2 != 0):
            ans = 0
        elif(boy % 2 != 0):
            ans = 1
        n /= 2
        boy /= 2
    if(ans==1):
        numbers.append(tempb)

print(len(numbers))
for i in numbers:
    print(i,end=" ")
