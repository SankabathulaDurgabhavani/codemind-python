n=int(input())
s=0
p=n*n
while(p!=0):
    r=p%10
    s=s+r
    p=p//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")