n=int(input())
m=int(input())
for i in range(n,m):
    s=0
    o=i
    while(i!=0):
        r=i%10;
        s=s*10+r;
        i=i//10;
        if(s==o):
            print(s,end=" ")
