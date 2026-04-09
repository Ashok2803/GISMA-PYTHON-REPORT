from customer import Customer
from account import BankAccount
from transaction import Transaction
from datetime import datetime
import uuid


class BankSystem:
    """A class to manage the entire bank system"""
    
    def __init__(self):
        """Initialize the bank system"""
        self.customers = {}  # customer_id -> BankCustomer
        self.accounts = {}   # account_number -> BankAccount
        self.transactions = {}  # transaction_id -> Transaction
        self.next_customer_id = 1
        self.next_account_number = 100000
    
    def add_customer(self, name, email, phone, address):
        """Add a new customer to the system"""
        customer_id = f"CUST{self.next_customer_id:04d}"
        self.next_customer_id += 1
        customer = Customer(customer_id, name, email, phone, address)
        self.customers[customer_id] = customer
        return customer_id
    
    def get_customer(self, customer_id):
        """Get customer by ID"""
        return self.customers.get(customer_id)
    
    def add_account(self, customer_id, account_type="checking", initial_balance=0.0):
        """Add a new account for a customer"""
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        
        account_number = f"ACC{self.next_account_number:06d}"
        self.next_account_number += 1
        account = BankAccount(account_number, customer_id, account_type, initial_balance)
        self.accounts[account_number] = account
        self.customers[customer_id].add_account(account)
        return account_number
    
    def get_account(self, account_number):
        """Get account by number"""
        return self.accounts.get(account_number)
    
    def process_deposit(self, account_number, amount):
        """Process a deposit transaction"""
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found")
        
        if account.deposit(amount):
            transaction_id = str(uuid.uuid4())
            transaction = Transaction(transaction_id, account_number, "deposit", amount, 
                                    balance_after=account.balance)
            self.transactions[transaction_id] = transaction
            return transaction_id
        return None
    
    def process_withdrawal(self, account_number, amount):
        """Process a withdrawal transaction"""
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found")
        
        if account.withdraw(amount):
            transaction_id = str(uuid.uuid4())
            transaction = Transaction(transaction_id, account_number, "withdrawal", amount,
                                    balance_after=account.balance)
            self.transactions[transaction_id] = transaction
            return transaction_id
        return None
    
    def process_transfer(self, from_account, to_account, amount):
        """Process a transfer between accounts"""
        from_acc = self.get_account(from_account)
        to_acc = self.get_account(to_account)
        if not from_acc or not to_acc:
            raise ValueError("One or both accounts not found")
        
        if from_acc.transfer(to_acc, amount):
            # Create transactions for both accounts
            transaction_id1 = str(uuid.uuid4())
            transaction_id2 = str(uuid.uuid4())
            
            trans1 = Transaction(transaction_id1, from_account, "transfer_out", amount,
                               f"Transfer to {to_account}", balance_after=from_acc.balance)
            trans2 = Transaction(transaction_id2, to_account, "transfer_in", amount,
                               f"Transfer from {from_account}", balance_after=to_acc.balance)
            
            self.transactions[transaction_id1] = trans1
            self.transactions[transaction_id2] = trans2
            return transaction_id1, transaction_id2
        return None
    
    def get_customer_accounts(self, customer_id):
        """Get all accounts for a customer"""
        customer = self.get_customer(customer_id)
        return customer.accounts if customer else []
    
    def get_account_transactions(self, account_number):
        """Get all transactions for an account"""
        return [trans for trans in self.transactions.values() if trans.account_number == account_number]
    
    def get_system_summary(self):
        """Get overall system statistics"""
        total_customers = len(self.customers)
        total_accounts = len(self.accounts)
        total_transactions = len(self.transactions)
        total_balance = sum(acc.balance for acc in self.accounts.values())
        
        return {
            'total_customers': total_customers,
            'total_accounts': total_accounts,
            'total_transactions': total_transactions,
            'total_balance': total_balance
        }
