n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
e=[]
for i in range(0,n):
    if a>s[i] or b<s[i]:
        e.append(s[i])
if e:
    print(max(e))
else:
    print('-1')