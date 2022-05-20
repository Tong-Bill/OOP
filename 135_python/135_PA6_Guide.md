# ProgrammingAssignment6

## Project Goals
The goal of this project is to:
1.	Familiarize students with the use of **arrays of strings**
2.  Familiarize students with **passing arrays of strings to functions**.
### Important Notes:
1.	**Formatting**: Make sure that you follow the precise recommendations for the output content and formatting. Your assignment will be auto-graded and any changes in formatting will result in a loss in the grade.
2.	**Comments**: Header comments are required on all files and recommended for the rest of the program. Points will be deducted if no header comments are included.
3.	**Filename**: Save your program as ```text_analyzer.c```

## Program
Roses are red. Violets are blue. We'll analyze a poem and write code, too.  

Write a program for analyzing text loaded from a file. The name of the inventory file should be saved as a macro. If the file can be opened for reading, each word should be read from the file. The program should count and display the total number of letters to the screen.

### The example executable:
An example executable is provided in this repository. You should be able to run it from your project folder.
If you encounter a "permission denied" error when attempting to run the executable, type ```chmod u+x analyzerExecutable``` into the terminal and try running the executable again.

## Requirements
*main()*  
**Functionality**: The main function should attempt to open the file. If it cannot open the input file for reading, it should display an error message (including the file name). If it can open the input file for reading, it should get the words from the file, save them to memory, and close the file. It should then count the number of letters, lower case letters, and vowels in each word. Finally, it should display the total number of letters, lower case letters, and vowels in all the words to the screen. 

All file opening and closing should occur in the main function. In addition to the main functions, your program should have at minimum 4 more functions:

In addition to the main function, your program should have 4 more functions:  

*getWords()*  
**Input Parameters**: integer max size of word, array of strings, file pointer  
**Returned Output**: integer number of words  
**Functionality**: This function should accept a file pointer which has already been connected to a file stream, an array of strings for storing each of the words, and a size parameter for the column. It should get each of the words from the file one at a time and store it into the array of strings. Finally, it should return the number of words it successfully pulled from the file.  

*countLetters()*  
**Input Parameters**: a single string  
**Returned Output**: integer number of letters in the word  
**Functionality**: This function should accept as a parameter a single string which stores one word. It should iterate over the string and count how many of characters are letters (not punctuation). Finally, it should return the number of letters found. 

*countLowerCase()*  
**Input Parameters**: a single string  
**Returned Output**: integer number of lower case letters in the word  
**Functionality**: This function should accept as a parameter a single string which stores one word. It should iterate over the string and count how many of characters are lower-case letters. Finally, it should return the number of lower-case letters found  

*countVowels()*  
**Input Parameters**: a single string  
**Returned Output**: integer number of vowels in the word  
**Functionality**: This function should accept as a parameter a single string which stores one word. It should iterate over the string and count how many of characters are vowels (upper and lower case). Finally, it should return the number of vowels found.  

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
