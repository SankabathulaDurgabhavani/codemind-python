n=int(input())
d=0
c=0
s=list(map(int,input().split()))
for i in range(0,n):
    if i%2==0:
        d=d+s[i]
    else:
        c=c+s[i]
print(abs(d-c))
