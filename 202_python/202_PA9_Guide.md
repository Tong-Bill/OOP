# ProgrammingAssignment9

## Project Goals
The goal of this project is to:
1.	Continued use of **Templates**.
3.  Provide practice with new **Recursion** skills.
### Important Notes:
1.	**Formatting**: Make sure that you follow the precise recommendations for the output content and formatting. For example, do not change the text from 
“Correct usage: ” to “correct”. 
Your assignment will be auto-graded and any changes in formatting will result in a loss in the grade.
2.	**Comments**: Header comments are required on all files and recommended for the rest of the program. Points will be deducted if no header comments are included.
## Program
Your project should include the following files:
```
- driver.cpp
- calculator.cpp
- calculator.h
- complex.cpp
- complex.h
- fraction.cpp
- fraction.h
- makefile  
```
Your executable should be named ```calculator```
## Programming Problem
Write a calculator program which operates in multiple modes.

### The example executable:
An example executable is provided in this repository. You should be able to run it from your project folder.
If you encounter a “permission denied” error when attempting to run the executable, type ```chmod u+x calculatorExecutable``` into the terminal and try running the executable again.  
## Requirements
```
driver.cpp
```
*main()*  
**Functionality**: The main function should display the types of calculator modes and allow the user to choose one. If the user chooses Option 1, the program should run an integer calculator. If the user chooses Option 2, the program should run a floating point calculator. If the user chooses Option 3, the program should run a complex number calculator. If the user chooses Option 4, the program should run a fraction calculator. The program should exit if the user chooses Option 0, and an error message should be displayed if the user does not choose a valid option.  

In addition to the main functions, your driver should have at minimum 6 more functions:

*getCalcType()*  
**Input Parameters**: none  
**Returned Output**: integer number corresponding to the calculator type  
**Functionality**: This function should display the calculator mode options to the screen. It should get the user's choice and return it to the calling function.

*getOperation()*  
**Input Parameters**: none  
**Returned Output**: integer number corresponding to the arithmetic operation  
**Functionality**: This function should display the caculator arithmetic operations to the screen. It should get the user's choice and return it to the calling function.

*integerCalculator()*  
**Input Parameters**: none  
**Returned Output**: none  
**Functionality**: This function should create the appropriate calculator. It should prompt the user for the arithmetic operation. If the user did not choose Option 0, they should be prompted for the operands. The appropriate result should be displayed to the user, based on the arithmetic operation the user chose. Don't forget, you can't divide by zero!

*floatingCalculator()*  
**Input Parameters**: none 
**Returned Output**: none  
**Functionality**: This function should create the appropriate calculator. It should prompt the user for the arithmetic operation. If the user did not choose Option 0, they should be prompted for the operands. The appropriate result should be displayed to the user, based on the arithmetic operation the user chose. Don't forget, you can't divide by zero!

*complexCalculator()*  
**Input Parameters**: none    
**Returned Output**: none  
**Functionality**: This function should create the appropriate calculator. It should prompt the user for the arithmetic operation. If the user did not choose Option 0 or Option 4, they should be prompted for the operands. The appropriate result should be displayed to the user, based on the arithmetic operation the user chose. Don't forget, you can't perform division on a complex number!  

*fractionCalculator()*  
**Input Parameters**: none    
**Returned Output**: none  
**Functionality**: This function should create the appropriate calculator. It should prompt the user for the arithmetic operation. If the user did not choose Option 0, they should be prompted for the operands. The appropriate result should be displayed to the user, based on the arithmetic operation the user chose. Don't forget, you cannot have a 0 denominator!  

```
caclulator.h
```
**Functionality**: This file should contain the definition for the templated Calculator class, which includes the following attributes:  
```
operand1
operand2
```
```
caclulator.cpp
```
**Functionality**: This file should contain the function definitions for the following functions:

*Constructors*  
- default constructor
- parameterized contructor

*Getters*  
Getter functions for each attribute.   

*getOperands()*  
**Input Parameters**: none  
**Returned Output**: none  
**Functionality**: This function should prompt the user for each operand and save the user input in the appropriate operand.  

*addition()*  
**Input Parameters**: none  
**Returned Output**: template item  
**Functionality**: This function should return the result of addition the two operands together. 

*subtraction()*  
**Input Parameters**: none  
**Returned Output**: template item   
**Functionality**: This function should return the result of subtraction the second operand from the first operand.  

*multiplication()*  
**Input Parameters**: none  
**Returned Output**: template item   
**Functionality**: This function should return the result of multiplication the two operands together.  

*division()*  
**Input Parameters**: none  
**Returned Output**: template item   
**Functionality**: This function should return the result of dividng the first operand by the second operand.  
```
complex.h
```
**Functionality**: This file should contain the definition for the Complex class, which includes the following attributes:  
```
double real
double imaginary
```
```
complex.cpp
```
**Functionality**: This file should contain the function definitions for the following functions:

*Constructors*  
- default constructor
- parameterized contructor

*Getters*  
Getter functions for each attribute. 

*Setters*  
Setter functions for each attribute.  

*operator+()*  
**Input Parameters**: constant Complex reference  
**Returned Output**: Complex  
**Functionality**: This function create a new Complex object. It's real part should be the sum of the current object's real part and the parameter's real part. It's imaginary part should be the sum of the current object's imaginary part and the parameter's imaginary part. The new Complex object should be returned from the function.  

*operator-()*  
**Input Parameters**: constant Complex reference  
**Returned Output**: Complex  
**Functionality**: This function create a new Complex object. It's real part should be the difference of the current object's real part and the parameter's real part. It's imaginary part should be the differenct of the current object's imaginary part and the parameter's imaginary part. The new Complex object should be returned from the function.  

*operator\*()*  
**Input Parameters**: constant Complex reference  
**Returned Output**: Complex  
**Functionality**: This function create a new Complex object. It's real part should be the difference of the products of the real parts and the imaginary parts. It's imaginary part should be the sum of product of the current object's real part and the parameter's imaginary part, and the product of the current object's imaginary part and the parameter's real part. The new Complex object should be returned from the function.  

*operator>>*  
**Input Parameters**: istream reference, Complex reference  
**Returned Output**: istream reference  
**Functionality**: This function should prompt the user for the real and imaginary components of the complex number and save those values in the Complex object parameter.  

*operator<<*  
**Input Parameters**: ostream reference, Complex  
**Returned Output**: ostream reference  
**Functionality**: This function should display the real component of the Complext object parameter. If the imaginary component exists and is positive, it should display a plus sign, otherwise a minus sign. If the imaginary component exists, it should be displayed to the screen.  
```
fraction.h
```
**Functionality**: This file should contain the definition for the Fraction class, which includes the following attributes:  
```
int numerator
int denominator
```
```
fraction.cpp
```
**Functionality**: This file should contain the function definitions for the following functions:

*greatestCommonDivisor*
**Input Parameters**: integer divisor, integer divisor
**Returned Output**: integer
**Functionality**:  This function ***recursively*** finds the greatest common divisor between the two input parameters. https://en.wikipedia.org/wiki/Recursion_(computer_science)#Recursive_programs  

*leastCommonMultiple*
**Input Parameters**: integer multiple, integer multiple
**Returned Output**: integer
**Functionality**:  This function calculates the least commone multiple by determining the product of the two multiples, divided by the greatest common divisor.

*Constructors*  
- default constructor
- parameterized contructor

*Getters*  
Getter functions for each attribute. 

*Setters*  
Setter functions for each attribute. *Remember* fractions cannot have a 0 denominator.  

*operator+()*  
**Input Parameters**: constant Fraction reference  
**Returned Output**: Fraction  
**Functionality**: This function create a new Fraction object. It should find the least common denominator and add the fractions together. The new Fraction object should be returned from the function.  

*operator-()*  
**Input Parameters**: constant Fraction reference  
**Returned Output**: Fraction  
**Functionality**: This function create a new Fraction object. It should find the least common denominator and subtract the second fraction from the first. The new Fraction object should be returned from the function.    

*operator\*()*  
**Input Parameters**: constant Fraction reference  
**Returned Output**: Fraction  
**Functionality**: This function create a new Fraction object. The numerators and the denominators of each fraction should be multiplied together. The new Fraction object should be returned from the function.      

*operator/()*  
**Input Parameters**: constant Fraction reference  
**Returned Output**: Fraction  
**Functionality**: This function create a new Fraction object. The first fraction should be multiplied by the reciprocal of the second fraction. The new Fraction object should be returned from the function.  

*operator>>*  
**Input Parameters**: istream reference, Fraction reference  
**Returned Output**: istream reference  
**Functionality**: This function should get the numerator and the denominator of a fraction, separated by the forward slash character, '/'.  

*operator<<*  
**Input Parameters**: ostream reference, Fraction  
**Returned Output**: ostream reference  
**Functionality**: This function should display the numerator and the denominator of a fraction, separated by the forward slash character, '/'   

## Submission details
To submit your project, you will have to use git on your VirtualBox installation:
1.	After accepting the assignment invitation, copy the clone URL
2.	Type 
```git clone clone URL```
3.	cd into your new assignment directory
4.	After working on your files
5.	When you’re ready, type the following commands: 
```
git add .
git commit -m “a descriptive message!”
git push
```
## Academic Honesty
Academic dishonesty is against university as well as the system community standards. Academic dishonesty includes, but is not limited to, the following:
Plagiarism: defined as submitting the language, ideas, thoughts or work of another as one's own; or assisting in the act of plagiarism by allowing one's work to be used in this fashion.
Cheating: defined as (1) obtaining or providing unauthorized information during an examination through verbal, visual or unauthorized use of books, notes, text and other materials; (2) obtaining or providing information concerning all or part of an examination prior to that examination; (3) taking an examination for another student, or arranging for another person to take an exam in one's place; (4) altering or changing test answers after submittal for grading, grades after grades have been awarded, or other academic records once these are official.
Cheating, plagiarism or otherwise obtaining grades under false pretenses constitute academic
dishonesty according to the code of this university. Academic dishonesty will not be tolerated and
penalties can include cancelling a student’s enrolment without a grade, giving an F for the course, or for the assignment. For more details, see the University of Nevada, Reno General Catalog.
