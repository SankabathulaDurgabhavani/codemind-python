n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
e=[]
for i in range(0,n):
    if a>s[i] or b<s[i]:
        e.append(s[i])
if e:
    for i in e:
        print(i,end=" ")
else:
    print('-1')
