# ProgrammingAssignment3

## Project Goals
The goal of this project is to:
1.	Familiarize students with **loops**
2.  Familiarize students with the **file IO**.
### Important Notes:
1.	**Formatting**: Make sure that you follow the precise recommendations for the output content and formatting. Your assignment will be auto-graded and any changes in formatting will result in a loss in the grade.
2.	**Comments**: Header comments are required on all files and recommended for the rest of the program. Points will be deducted if no header comments are included.
3.	**Filename**: Save your program as ```student_info.c```

## Program
Managing Student Information!  

We're going to build a student information management system.   

The user should be shown a menu with four options: display student initials, display student GPAs, add students, or exit the program. If the user chooses to exit, the program should end. Otherwise, if the user chooses to display the student initials, the contents of the students.txt file should be read, and just the student number and initials should be displayed to the user in a tabular format. If the user chooses to display the student GPAs, the contents of the students.txt file should be read, and just the student number and GPAs should be displayed to the user in a tabular format. If the user chooses to add students, they should be prompted for the number of studnets they’d like to add. They should then be prompted that many times for a studnet number, a GPA, a first initial, and a last initial. Each of the new items should be saved to the students.txt file.

### The example executable:
An example executable is provided in this repository. You should be able to run it from your project folder.
If you encounter a "permission denied" error when attempting to run the executable, type ```chmod u+x studentExecutable``` into the terminal and try running the executable again.

## Requirements
*main()*  
**Functionality**: This main function should prompt the user for a menu option until they enter 4. It should decide, based on that menu option which actions to perform. Option 4 ends the program. Option 1 opens the students.txt file for reading and checks for a successful connection to the file stream. If it can, it will display the student initials, then close the file. Option 2 opens the students.txt file for reading and checks for a successful connection to the file stream. If it can, it will display the student GPAs, then close the file. Option 3 opens the studnets.txt for writing and checks for a successful connection to the file stream. If it can, it gets new students, then closes the file. Any other options should result in the error message.
In addition to the main functions, your program should have 4 more functions:

*getMenuChoice()*  
**Input Parameters**: none  
**Returned Output**: int  
**Functionality**: This function should display to the screen the options available to the user and return the users inputted menu choice.  

*displayStudentInitials()*  
**Input Parameters**: FILE pointer  
**Returned Output**: none  
**Functionality**: This function should accept a file pointer which has already been connected to a file stream. It should display a table of student numbers and student initials (with no spaces in between). Each of the values in the table should be read in from the students.txt file, but only the values specified should be in the table.  

*displayStudentGpas()*  
**Input Parameters**: FILE pointer  
**Returned Output**: none  
**Functionality**: This function should accept a file pointer which has already been connected to a file stream. It should display a table of student numbers and student GPAs (with a two decimal precision). Each of the values in the table should be read in from the students.txt file, but only the values specified should be in the table.  

*addStudents()*  
**Input Parameters**: FILE pointer  
**Returned Output**: none  
**Functionality**: This function should accept a file pointer which has already been connected to a file stream. It should prompt the user for the number of students they’d like to add. For each of those students, the user should be prompted for the five digit student number, gpa, first initial, and last initial, which should all be saved to the file.  

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
git commit -m “your commit message”
git push
```
## Academic Honesty
Academic dishonesty is against university as well as the system community standards. Academic dishonesty includes, but is not limited to, the following:
Plagiarism: defined as submitting the language, ideas, thoughts or work of another as one's own; or assisting in the act of plagiarism by allowing one's work to be used in this fashion.
Cheating: defined as (1) obtaining or providing unauthorized information during an examination through verbal, visual or unauthorized use of books, notes, text and other materials; (2) obtaining or providing information concerning all or part of an examination prior to that examination; (3) taking an examination for another student, or arranging for another person to take an exam in one's place; (4) altering or changing test answers after submittal for grading, grades after grades have been awarded, or other academic records once these are official.
Cheating, plagiarism or otherwise obtaining grades under false pretenses constitute academic
dishonesty according to the code of this university. Academic dishonesty will not be tolerated and
penalties can include cancelling a student’s enrolment without a grade, giving an F for the course, or for the assignment. For more details, see the University of Nevada, Reno General Catalog.
