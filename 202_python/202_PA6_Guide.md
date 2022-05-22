# ProgrammingAssignment6

## Project Goals
The goal of this project is to:
1.	Continued use of **makefiles**.
2.  Continued use of **class** building skills.
3.  Provide practice with new **Abstract Base Class** skills.
4.  Provide practice with new **virtual functions** skills.
### Important Notes:
1.	**Formatting**: Make sure that you follow the precise recommendations for the output content and formatting. For example, do not change the text from 
“Correct usage: ” to “correct”. 
Your assignment will be auto-graded and any changes in formatting will result in a loss in the grade.
2.	**Comments**: Header comments are required on all files and recommended for the rest of the program. Points will be deducted if no header comments are included.
## Program
Your project should include the following files:
```
- driver.cpp
- pet.cpp
- pet.h
- cat.cpp
- cat.h
- bird.cpp
- bird.h
- fish.cpp
- fish.h
- makefile  
```
Your executable should be named ```pets```
## Programming Problem
Write a program for managing some pets.

### The example executable:
An example executable is provided in this repository. You should be able to run it from your project folder.
If you encounter a “permission denied” error when attempting to run the executable, type ```chmod u+x petsExecutable``` into the terminal and try running the executable again  
## Requirements
```
driver.cpp
```
*main()*  
**Functionality**: The main function should manage a Cat, a Fish, and a Bird. It should get information for setting the attribute of each pet. It should then feed each pet and let them play!  

In addition to the main functions, your driver should have at minimum 4 more functions:

*getCat()*  
**Input Parameters**: Cat  
**Returned Output**: None  
**Functionality**: This function should accept a Cat whose attributes will be set. The user should be prompted for the Cat's name, number of legs, and whether or not it has a tail. Those values should be saved to that Cat.

*getFish()*  
**Input Parameters**: Fish  
**Returned Output**: None  
**Functionality**: This function should accept a Fish whose attributes will be set. The user should be prompted for the Fish's name and whether or not it has a tail. Those values should be saved to that Fish.

*getBird()*  
**Input Parameters**: Bird  
**Returned Output**: None  
**Functionality**: This function should accept a Bird whose attributes will be set. The user should be prompted for the Bird's name and number of legs. Those values should be saved to that Bird.

*feedPet()*  
**Input Parameters**: Pet pointer  
**Returned Output**: None  
**Functionality**: This function should prompt the user for the kind of food to feed the pet and then allow the pet to eat that food.  
```
pet.h
```
**Functionality**: This file should contain the definition for the Pet class, which includes the following attributes:  
```
int legs
bool tail
string name
```
```
pet.cpp
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

*Pure Virtual Functions*  
*eat()*  
**Input Parameters**: constant string  
**Returned Output**: none  
```
cat.h
```
**Functionality**: This file should contain the definition for the Cat class. It should inherit from the Pet class.  
```
cat.cpp
```
**Functionality**: This file should contain the function definitions for the following functions:

*Constructors*  
- default constructor
- parameterized contructor

*pounce()*  
**Input Parameters**: None  
**Returned Output**: None  
**Functionality**: This function should dispaly a pouncing message to the screen. If the cat has more than 2 legs, it should display "RAWR!" to the screen. Otherwise, it should display "meow" to the screen.  

*eat()*  
**Input Parameters**: string  
**Returned Output**: none  
**Functionality**: This function should display the message that the cat is "devouring my" food.  
```
fish.h
```
**Functionality**: This file should contain the definition for the Fish class. It should inherit from the Pet class.
```
fish.cpp
```
**Functionality**: This file should contain the function definitions for the following functions:

*Constructors*  
- default constructor
- parameterized contructor

*swim()*  
**Input Parameters**: None  
**Returned Output**: None  
**Functionality**: This function should dispaly a swimming message to the screen. If the fish has a tail, it should display "Just keep swimming!" to the screen. Otherwise, it should display "glub glub" to the screen. 

*eat()*  
**Input Parameters**: string  
**Returned Output**: none  
**Functionality**: This function should display the message that the fish is "slurping my" food.  
```
bird.h
```
**Functionality**: This file should contain the definition for the Bird class. It should inherit from the Pet class.
```
bird.cpp
```
**Functionality**: This file should contain the function definitions for the following functions:

*Constructors*  
- default constructor
- parameterized contructor

*fly()*  
**Input Parameters**: none  
**Returned Output**: none  
**Functionality**: This function should dispaly a flying message to the screen. If the bird has a tail, it should display "Fly like the wind!" to the screen. Otherwise, it should display "hop along" to the screen.  

*eat()*  
**Input Parameters**: string  
**Returned Output**: none  
**Functionality**: This function should display the message that the bird is "pecking at my" food.  

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
