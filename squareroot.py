# defining a fuction to calculate the square root of a positive real number
# using Newton's method

A = int(input("Input value to find square root "))

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

     