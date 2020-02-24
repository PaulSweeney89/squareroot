# defining a fuction to calculate the square root of a positive real number
# using Newton's method (ALTERNATIVE)

while True:                         

    A = float(input("Please input positive value "))

    if A > 0:                       
        break                       
    
    else:                           
        print(A, " is a negative value")
        continue

def sqrt(A):                        
    x = 1                           

    for n in range(0, 10):                # using a for loop with 10 iterations    
        f1 = (x * x - A)            
        f2 = 2 * x                  
        x = (x - (f1 / f2))
        n = n + 1         
        if f1 == 0:     
            break                   
    return (x)                      

ans = sqrt(A)

print("The square root of ", A , "is ", ans)
