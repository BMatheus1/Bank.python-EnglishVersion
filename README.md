🏦 Bank Account Management System (Python)

A simple and educational Bank Account Management System built in Python using Object-Oriented Programming (OOP) and a terminal-based interactive menu.

This project simulates basic banking operations such as adding clients, listing accounts, and toggling an account’s active status.

Ideal for beginners learning Python OOP and terminal application structure.

✨ Features
✔️ Add new clients

Each client contains:

Full name (auto formatted)

Initial balance

CPF (with automatic formatting to 000.000.000-00)

Profession

Account status (active/inactive)

✔️ List all clients

Displays clients in a formatted table with:

Name

Balance

CPF

Profession

Account status

✔️ Activate or deactivate an account

Search clients by CPF

Accepts CPF typed with or without dots and hyphens

Toggles between Active ✔️ and Inactive ❌

✔️ Interactive menu

Clear terminal presentation

Option navigation

Return to main menu

Clean exit

🧠 Concepts Used

This project was built using key programming concepts:

Classes and objects

Encapsulation with protected attributes

@staticmethod for utility functions (CPF formatting)

@classmethod for creating accounts and listing clients

Properties (@property) for computed status

Input validation

String manipulation and formatting

Loops and menu systems (while True)

Clean terminal UI (os.system('cls'))

🛠️ Improvements Over the Original Version

The original project only supported:

Client name

Balance

Account status

The new version adds significant improvements:

🔹 New client fields

CPF (automatically formatted)

Profession

Normalization of names and text formatting

🔹 Stronger lookup system

Search by formatted CPF

User input cleaned and converted automatically

🔹 Improved table layout

Aligned columns

Clear terminal output

🔹 Menu structure improved

Cleaner control flow

Proper returning to main menu

Clean program exit

▶️ How to Run

Make sure you have Python installed.

In the terminal:

python bank.py

📁 Project Structure
project/
│── bank.py       # Main script containing the OOP banking system

🔮 Future Enhancements

Possible improvements include:

Client removal system

Deposit and withdrawal operations

Account transaction history (extract)

Persisting data in JSON or database

Generating unique account numbers

Adding a GUI with Tkinter or PyQt

Password-protected accounts

📌 Purpose of the Project

This project was created to practice:

Object-Oriented Programming

Code organization and architecture

User interaction via terminal

Handling and validating user input

Building scalable menu-driven applications
