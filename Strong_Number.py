def fac(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
n=int(input())
t=n
s=0
while n!=0:
    r=n%10
    s=s+fac(r)
    n//=10
if t==s:
    print('The number {} is a strong number'.format(t))
else:
    print('The number {} is not a strong number'.format(t))