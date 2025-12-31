🔐 Password Generator (Python)

A beginner-friendly, console-based password generator built using Python.  
The program generates a random password only after the user enters a specific command and provides the desired password length.

This project focuses on basic Python concepts such as string handling, conditional logic, loops, and input validation.

 Features

- Command-based execution (`password generator`)
- Generates random passwords using:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
- User-defined password length
- Input validation for invalid commands and non-numeric values
- Simple and clean console output

 Technical Details

- Language: Python 3.x
- Modules Used: `random`
- Core Concepts:
  - Strings and concatenation
  - Conditional statements
  - Exception handling (`try-except`)
  - Random sampling

No external libraries are required.
 How to Run

1. Clone the repository
   bash
   git clone https://github.com/Adikesavareddy-git/password-generator.git
Navigate to the project directory

bash
Copy code
cd password-generator
Run the program

bash
Copy code
python password_generator.py
 Program Flow
 User types password generator
Program asks for password length
Random password is generated
Password is displayed in the console
If the command is incorrect, the program stops.

 Limitations
 Uses random module (not cryptographically secure)
No password strength analysis
Console-based only
These limitations are acceptable for a beginner-level project.
Possible Enhancements
 Use secrets module for better security
Add password strength checker
Allow user to choose character types
Save generated passwords to a file
Build a GUI version

 Author
Adikesavareddy Katterapalli
GitHub: https://github.com/Adikesavareddy-git
LinkedIn: https://www.linkedin.com/in/adikesavareddy-katterapalli
