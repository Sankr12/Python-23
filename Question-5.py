# Create a generator to produce first n terms of fibonacci series

def fibonacciGenerator(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1

num = int(input("Enter a number: "))
for i in fibonacciGenerator(num):
    print(i,end=' ')