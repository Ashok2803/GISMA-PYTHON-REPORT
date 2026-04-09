from datetime import datetime


class BankAccount:
    """A class to represent a bank account"""
    
    def __init__(self, account_number, customer_id, account_type="checking", initial_balance=0.0):
        """
        Initialize a bank account
        
        Args:
            account_number (str): Unique account identifier
            customer_id (str): ID of the account holder
            account_type (str): Type of account (checking, savings, etc.)
            initial_balance (float): Starting balance
        """
        self.account_number = account_number
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = initial_balance
        self.created_date = datetime.now()
        self.transactions = []
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            self.transactions.append({
                'type': 'deposit',
                'amount': amount,
                'date': datetime.now(),
                'balance_after': self.balance
            })
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append({
                'type': 'withdrawal',
                'amount': amount,
                'date': datetime.now(),
                'balance_after': self.balance
            })
            return True
        return False
    
    def get_balance(self):
        """Get current account balance"""
        return self.balance 

    def transfer(self, target_account, amount):
        """Transfer money to another account"""
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False
    
    def display_account_info(self):
        """Display account information"""
        print(f"Account Number: {self.account_number}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Created: {self.created_date.strftime('%Y-%m-%d')}")
        print(f"Transaction Count: {len(self.transactions)}")
    
    def __str__(self):
        """String representation of account"""
        return f"{self.account_type.capitalize()} Account {self.account_number} - Balance: ${self.balance:.2f}"
    
    def __repr__(self):
        """Official string representation"""
        return f"BankAccount('{self.account_number}', '{self.customer_id}', '{self.account_type}', {self.balance})"
