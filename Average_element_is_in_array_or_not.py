n=int(input())
s=0
l=list(map(int,input().split()))
for i in range(0,n):
    s=s+l[i]
d=s//n
if d in l:
    print(True)
else:
    print(False)
    