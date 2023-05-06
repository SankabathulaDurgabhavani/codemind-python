n=int(input())
p=n*n
s=0
while(p!=0):
    r=p%10
    s=s+r
    p=p//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")