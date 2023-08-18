# Create a generator to produce sqaures of first n natural numbers

def SquareGenerator(n):
    x=1
    while n:
        yield x**2
        x+=1
        n-=1

num = int(input("Enter a number: "))
l1 = list(i for i in SquareGenerator(num))
print(l1)