# Create a generator to produce first n prime numbers

def PrimeGenerator(n):
    a=2
    while n:
        for i in range(2,a):
            if a%i==0:
                a+=1
                break
        else:
            yield a
            n-=1
            a+=1

num = int(input("Enter a number: "))
for i in PrimeGenerator(num):
    print(i,end=' ')