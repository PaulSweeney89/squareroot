# defining a fuction to calculate the square root of a positive real number
# using Newton's method

A = float(input("Please input positive value "))

def sqrt(A):
    x = A
    f1 = x * x - A
    f2 = 2 * x
    x = x - (f1 / f2)
    
    while x > 0:
        f1 = x * x - A
        f2 = 2 * x
        x = x - (f1 / f2)
        if f1 == 0:
            break
    return x

print(sqrt(A))

# code doesn't work with non-straight forward square roots
# look at using floor function to find approx square roots for tricky values
     