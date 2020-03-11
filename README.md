# squareroot
**Defining a function to calculate the square root of a inputted number using Newton's Method.**

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
  - x = x - f1 / f2           (solving for a better approximation of x using Newton's method, see screenshot below.)
  
  ![Wikipedia Screenshot](https://user-images.githubusercontent.com/60242385/75181783-eb8da300-5736-11ea-8cb0-71d8f4aa2317.png)
  
  - while loop re-iterates using the improved approximation value of x each time until x^2 - A = 0 or in other words we solve for x the square root value of A.
  - For straight forward sqrt numbers i.e, 4, 16, 36 this method works well. However for non-straight forward sqrt numbers the approximate value for x can never fully reach the actual sqrt value of A and therefore the while loop ends up in a infinite loop (x^2 - A never reaches 0 for certain numbers). Therefore the math.floor() function has been introduced to force the function to converge on zero.
- Therefore the program only gives approximate values for the **sqrt(A)** and so the program results have been rounded to 1 decimal place.

Example of input & output of Program:
```
python squareroot.py
Please input positive value 14.5
The square root of  14.5 is  3.8
```

Comments:

1. By taking the unrounded square root value calculated in the program and comparing it to the value calculated using the google sheet linked below, it was found that program didn't calculate the square root value as accurately as the spreadsheet. 

Program result:
>3.8092816328050976

Google Sheet Result (5 iternations):
>3.807886553

2. This is due to using the math.floor() function, which ends up forcing the f1 function to converge on zero, mostly likely reducing the number of internations & approximations for x.

3. A possible improvement to the program and the accurancy of the squareroot calculation would be to replace the 'while x > 0 loop' with a 'for loop' with either a user defined or fixed number of iternations, while also removing the math.floor() function.

See sqrt_test.py script included in repository.

References:

[Newton's Method Wikipedia](https://en.wikipedia.org/wiki/Newton's_method)

[Finding square root using Newton's Method - Jerry L. Kazdan](https://www.math.upenn.edu/~kazdan/202F09/sqrt.pdf)

[Newton's Method Youtube](https://www.youtube.com/watch?v=1uN8cBGVpfs)

[Google Sheet Newton's Method Test](https://docs.google.com/spreadsheets/d/1XdYph3rWyFUW1V87tzbpFzPePt--ykv3IMzU9g2qohI/edit?usp=sharing)

[While True Loop](https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input)

