# Create an endless iterator using generator method to produce terms of Fibonacci series

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Test the generator
fibonacci_iter = fibonacci_generator()

try:
    while True:
        next_fibonacci = next(fibonacci_iter)
        print(next_fibonacci)
        ask = input("Do you want to print the next Fibonacci term [y/n]: ")
        if ask != 'y':
            break
except KeyboardInterrupt:
    print("Generator stopped by user")
