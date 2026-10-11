# Password Strength Checker 🔐

## About the Project

The Password Strength Checker is a Python project developed using Tkinter. It checks the strength of a password based on its length and character types.

I developed this project to learn Python GUI development and understand the basics of password security. The application has a simple dark-themed interface that shows password strength and provides helpful tips for creating stronger passwords.

## Features

* User-friendly graphical interface.
* Checks password strength in real time.
* Displays a password strength score out of 5.
* Shows a visual strength meter.
* Checks password length, uppercase letters, lowercase letters, numbers, and symbols.
* Allows users to show or hide their passwords.
* Displays password requirements with status indicators.
* Provides helpful tips for creating stronger passwords.
* Checks passwords locally without sending them to an external server.

## Technologies Used

* Python
* Tkinter
* String module
* Visual Studio Code

## How It Works

The application checks whether the password meets five basic requirements:

1. Contains at least 12 characters.
2. Contains an uppercase letter.
3. Contains a lowercase letter.
4. Contains a number.
5. Contains a symbol.

Each satisfied requirement adds one point to the total score.

Based on the score, the application displays the password strength as Weak, Medium, or Strong. The strength meter and requirement indicators update as the user types.

## How to Run the Project

1. Install Python on your computer.
2. Download or clone this project.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Run the following command:

```bash
python password_checker.py
```

6. The application window will open.
7. Enter a password and check its strength.

## Project Structure

```text
Password-Strength-Checker/
│
├── password_checker.py
└── README.md
```

## What I Learned

Through this project, I learned how to use Python classes, functions, conditional statements, and string operations. I also learned how to create a graphical user interface using Tkinter, update interface elements dynamically, and use events to respond to user input.

This project also helped me understand the importance of password length, character variety, and using unique passwords.

## Future Improvements

* Add a strong password generator.
* Improve the password-strength assessment.
* Add checks for commonly used passwords.
* Improve the interface with additional customization options.
* Add more password security recommendations.

## Conclusion

This project helped me improve my Python programming skills and understand basic password security concepts. It also gave me practical experience in developing a graphical application using Tkinter.

The project is intended for educational purposes and provides a simple way to understand password-strength checking.

## Author

Developed as a Python and cybersecurity learning project.
