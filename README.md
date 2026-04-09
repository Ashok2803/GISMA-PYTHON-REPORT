# GISMA-PYTHON-REPORT
A simple banking system built in Python that lets you create customers, manage their accounts, and handle everyday transactions like deposits, withdrawals, and transfers. Everything gets logged and saved to a CSV file so your data sticks around between sessions.
clone the repository
https://github.com/Ashok2803/python.git
ensure python 3 is installed                                                                                                     check your version:                                                                                                               python3 ----version
run the program                                                                                                                   python3 main.py

list of key features and files                                                    
Customer Management — Create customers with personal details (name, email, phone, address); track membership start date automatically
Account Operations — Deposit, withdraw, and transfer funds between accounts with balance validation
Transaction Logging — Every transaction recorded with a unique UUID, timestamp, type, amount, and running balance
CLI Interface — Numbered menu with 12 options, success/failure indicators (✓/✗), and immediate feedback after each operation
Data Persistence — Customer data saved to and loaded from CSV files using Python's built-in csv.DictWriter/DictReader
Transaction Reports — Human-readable plain text reports with formatted headers and separators
