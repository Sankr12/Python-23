# Create a generate to produce first n even natural numbers

def evengenerator(n):
    x=2
    while n:
        yield x
        x+=2
        n-=1

num = int(input("Enter a number: "))
for i in evengenerator(num):
    print(i,end=' ')
