n=int(input())
r=0
s=0
m=1
while(n!=0):
    re=n%10
    r=r+re
    m=m*re
    n=n//10
if r==m:
    print("Spy Number")
else:
    print("Not Spy Number")