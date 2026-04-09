from datetime import datetime


class Customer:
    """A class to represent a bank customer"""
    
    def __init__(self, customer_id, name, email, phone, address):
        """
        Initialize a bank customer
        
        Args:
            customer_id (str): Unique customer identifier
            name (str): Customer's full name
            email (str): Customer's email address
            phone (str): Customer's phone number
            address (str): Customer's address
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.accounts = []
        self.created_date = datetime.now()
    
    def add_account(self, account):
        """Add a bank account to the customer"""
        self.accounts.append(account)
    
    def remove_account(self, account_number):
        """Remove a bank account by account number"""
        self.accounts = [acc for acc in self.accounts if acc.account_number != account_number]
    
    def get_total_balance(self):
        """Calculate total balance across all accounts"""
        return sum(account.balance for account in self.accounts)

    def get_account_count(self):
        """Return number of accounts the customer has"""
        return len(self.accounts)
    
    def display_customer_info(self):
        """Display customer information"""
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"Number of Accounts: {self.get_account_count()}")
        print(f"Total Balance: ${self.get_total_balance():.2f}")
        print(f"Member Since: {self.created_date.strftime('%Y-%m-%d')}")
    
    def __str__(self):
        """String representation of customer"""
        return f"{self.name} (ID: {self.customer_id})"
    
    def __repr__(self):
        """Official string representation"""
        return f"BankCustomer('{self.customer_id}', '{self.name}')"
