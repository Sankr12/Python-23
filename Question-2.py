# Create a generate to produce first n odd natural numbers

def oddgenerator(n):
    x=1
    while n:
        yield x
        x+=2
        n-=1
num = int(input("Enter a number: "))
for i in oddgenerator(num):
    print(i,end=' ')
