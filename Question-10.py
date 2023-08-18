# Define a function which calculates HCF of two numbers. Define and apply a
# decorator to check whether two given numbers are co-prime or not.

def coprime_decorator(func):
    def wrapper(a, b):
        if hcf(a, b) == 1:
            return func(a, b)
        else:
            return "Not co-prime numbers"
    return wrapper

def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

@coprime_decorator
def calculate_hcf(a, b):
    return hcf(a, b)

# Test the decorated function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf_result = calculate_hcf(num1, num2)
print("HCF of", num1, "and", num2, "is", hcf_result)
