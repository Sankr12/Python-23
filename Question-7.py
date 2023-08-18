# Create an endless iterator using generator method to produce prime numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def endlessprime():
    num = 2
    primes = []
    while True:
        if is_prime(num):
            primes.append(num)
            yield num
        num += 1

PrimeGenerator = endlessprime()

try:
    while True:
        nextprime = next(PrimeGenerator)
        print(nextprime)
        ask = input("Do you want to print the next item[y/n]: ")
        if ask != "y":
            break
        else:
            print(next(PrimeGenerator))
except StopIteration:
    print("No more prime numbers to generate")
