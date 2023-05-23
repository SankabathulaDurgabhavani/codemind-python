n=int(input())
c=0
rev=0
while(n):
    r=n%10
    rev=rev*10+r
    c=c+1
    n=n//10
if((c==10) and (r!=0)):
    print("Valid")
else:
    print("Invalid")