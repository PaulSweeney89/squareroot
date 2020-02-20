# defining a fuction to calculate the square root of a positive real number
# using Newton's method

import math

while True:                         # While loop to loop input prompt until value inputted is positive.

    A = float(input("Please input positive value ")

    if A > 0:                       # If input value is positive break the 
        break                       # while loop and proceed with program execution.
    
    else:                           # If input value is negative continue while loop, re-promting input.
        print(A, " is a negative value")
        continue

def sqrt(A):                        # Define fuction called sqrt with argument A.
    x = 1                           # Taking initially x = 1

    while x > 0:                    # Run while load for values greater than 0.
        f1 = (x * x - A)            # Function 1 of Newton's Method.
        f2 = 2 * x                  # Fuction 2 of Netwon's Method.
        x = (x - (f1 / f2))         # Improved approximation value for x.
        if math.floor(f1) == 0:     # If statement to break while loop, when
            break                   # f1 = x^2 - A approaches 0, math.floor() used to force f1 to reach zero
    return (x)                      

ans = sqrt(A)

print("The square root of ", A , "is ", round(ans,1))       # sqrt value rounded to 1 decimal place.
# print(ans)