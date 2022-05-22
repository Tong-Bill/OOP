# ProgrammingAssignment10

## Project Goals
The goal of this project is to:
1.	Provide practice with new **Dynamic Memory Allocation** skills.
### Important Notes:
1.	**Formatting**: Make sure that you follow the precise recommendations for the output content and formatting. For example, do not change the text from 
“Correct usage: ” to “correct”. 
Your assignment will be auto-graded and any changes in formatting will result in a loss in the grade.
2.	**Comments**: Header comments are required on all files and recommended for the rest of the program. Points will be deducted if no header comments are included.
## Program
Your project should include the following files:
```
- driver.cpp
- team.cpp
- team.h
- student.cpp
- student.h
- makefile  
```
Your executable should be named ```team_mgmt```
## Programming Problem
Write a program which manages team rosters.

### The example executable:
An example executable is provided in this repository. You should be able to run it from your project folder.
If you encounter a “permission denied” error when attempting to run the executable, type ```chmod u+x teamExecutable``` into the terminal and try running the executable again.  
## Requirements
```
driver.cpp
```
*main()*  
**Functionality**: The main function should prompt the user for the team name, then how many students they'd like to add to the team roster. It should then prompt the user for each student. Finally, it should display the team to the screen.  
```
team.h
```
**Functionality**: This file should contain the definition for the Team class, which includes the following attributes:  
```
string team name
int number of students
Student* roster
```
```
team.cpp
```
**Functionality**: This file should contain the function definitions for the following functions:

*Constructors*  
- default constructor
- parameterized contructor
- copy constructor

*Destructor*  

*Getters*  
Getter functions for each attribute.   

*Setters*
Setter functions for Name and Roster (which includes setting the number of students)

*operator<<*  
**Input Parameters**: ostream reference, Team  
**Returned Output**: ostream reference  
**Functionality**: This function should display the name of the team and each student.  
```
student.h
```
**Functionality**: This file should contain the definition for the Student class, which includes the following attributes:  
```
string first name
string last name
int grade
```
```
student.cpp
```
**Functionality**: This file should contain the function definitions for the following functions:

*Constructors*  
- default constructor
- parameterized contructor
- copy constructor

*Getters*  
Getter functions for each attribute. 

*Setters*  
Setter functions for each attribute.  

*operator>>*  
**Input Parameters**: istream reference, Student reference  
**Returned Output**: istream reference  
**Functionality**: This function should get the Student's first name, last name, and grade (each separated by a space).  

*operator<<*  
**Input Parameters**: ostream reference, Student  
**Returned Output**: ostream reference  
**Functionality**: This function should display the last name, first name: grade of the Student.  

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
