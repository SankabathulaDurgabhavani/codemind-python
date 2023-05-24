x=int(input())
a=10
sq=0
i=0
while True:
    if x<a:
        sq=x**2
        d=sq%a
        if x==d:
            print("Automorphic Number")
            break
        else:
            print("Not an Automorphic Number")
            break
    a=a*10
    i+=1