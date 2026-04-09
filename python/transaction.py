from datetime import datetime


class Transaction:
    """A class to represent a bank transaction"""
    
    def __init__(self, transaction_id, account_number, transaction_type, amount, description="", balance_after=None):
        """
        Initialize a bank transaction
        
        Args:
            transaction_id (str): Unique transaction identifier
            account_number (str): Account involved in the transaction
            transaction_type (str): Type of transaction (deposit, withdrawal, transfer)
            amount (float): Transaction amount
            description (str): Optional description
            balance_after (float): Account balance after transaction
        """
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.date = datetime.now()
        self.balance_after = balance_after
    
    def is_debit(self):
        """Check if transaction is a debit (withdrawal or transfer out)"""
        return self.transaction_type in ['withdrawal', 'transfer_out']
    
    def is_credit(self):
        """Check if transaction is a credit (deposit or transfer in)"""
        return self.transaction_type in ['deposit', 'transfer_in']
    
    def get_formatted_amount(self):
        """Get amount with sign based on transaction type"""
        if self.is_debit():
            return f"-${self.amount:.2f}"
        else:
            return f"+${self.amount:.2f}"
    
    def display_transaction_info(self):
        """Display transaction information"""
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Account: {self.account_number}")
        print(f"Type: {self.transaction_type}")
        print(f"Amount: {self.get_formatted_amount()}")
        print(f"Description: {self.description}")
        print(f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")
        if self.balance_after is not None:
            print(f"Balance After: ${self.balance_after:.2f}")
    
    def __str__(self):
        """String representation of transaction"""
        return f"{self.transaction_type.capitalize()} of ${self.amount:.2f} on {self.date.strftime('%Y-%m-%d')}"
    
    def __repr__(self):
        """Official string representation"""
        return f"Transaction('{self.transaction_id}', '{self.account_number}', '{self.transaction_type}', {self.amount})"
