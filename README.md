# squareroot
**Defining a fuction to calculate the square root of a inputted number usign Newton's Method.**

*Week 6 Programming & Scripting Task*

Program Overview:

- Import math module to allow program access to math functions.
```
import math
```
- Program prompts the user to input a positive number 'A' to find the square root of 'A'.

- Program initialized with a while True loop to continously loop the input prompt until positive value for 'A' is entered.
  - Note the square root of a negative number is a complex number and is not within the reams of this program or task, therefore preventing the input of a negative value for 'A' has been incorporated into the program, with the below while loop.
```
while True:                         
    A = float(input("Please input positive value ")
    if A > 0:                       
        break                       
    else:                           
        print(A, " is a negative value")
        continue
```
- Define the function **sqrt(A)** with input argument 'A' using Netwon's Method.
  - Note refer to the reference links below for desciption of the method and the formulas used.
```
def sqrt(A): 
  x = 1
  while x > 0:
      f1 = (x * x - A)           
      f2 = 2 * x                 
      x = (x - (f1 / f2))         
      if math.floor(f1) == 0:     
           break                   
    return (x)
```
  - Initiate while loop, starting with x = 1 and loop for all values with x > 0 
  - Function 1: f1 = x^2 - A  (from A = x^2)
  - Function 2: f2 = 2 * x    (derivative of f1)
  - x = x - f1 / f2           (solving for a better approximation of x using Newton's method)
  - while loop re-iterates using the improved approximation value of x each time until x^2 - A = 0 or in other words we solve for x the square root value of A.
  - For straight forward sqrt numbers i.e, 4, 16, 36 this method works well. However for non-straight forward sqrt numbers the approximations values x can never fully reach the actual sqrt value of A and therefore the while loop ends up in a infinate loop (x^2 - A never reaches 0). Therefore the math.floor() function has been introduced to force the function to zero.
- Therefore the program only gives approximate values for the **sqrt(A)** and so the program results have been rounded to 1 decimal place.

Example of input & output of Program:


References

[Finding square root using Newton's Method](https://www.math.upenn.edu/~kazdan/202F09/sqrt.pdf])

[Newton's Method Youtube](https://www.youtube.com/watch?v=1uN8cBGVpfs)

[Google Sheet Newton's Method Test](https://docs.google.com/spreadsheets/d/1XdYph3rWyFUW1V87tzbpFzPePt--ykv3IMzU9g2qohI/edit?usp=sharing)

[While True Loop](https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input)

