# Use iter and next method to access all the elements of a given set using while loop

s1 = {1,2,3,4,5,6,7,8,9}
it = iter(s1)
try:
    while True:
        n = next(it)
        print(n)
except StopIteration:
    pass