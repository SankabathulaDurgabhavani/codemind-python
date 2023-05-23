# Multiplication table (from 1 to 10) in Python

a,b=map(int,input().split())

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1,b+1):
    if i%2!=0:
        print(a, 'x', i, '=', a*i)