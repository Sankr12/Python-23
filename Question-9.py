'''Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter of triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides.'''

def triangle_validator(func):
    def wrapper(a, b, c):
        if a + b > c and b + c > a and c + a > b:
            return func(a, b, c)
        else:
            return "Invalid triangle sides"
    return wrapper

@triangle_validator
def calculate_perimeter(a, b, c):
    return a + b + c

# Test the decorated function
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

perimeter = calculate_perimeter(side1, side2, side3)
print("Perimeter of the triangle:", perimeter)
