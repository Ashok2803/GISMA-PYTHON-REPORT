from banksystem import BankSystem
from customer import Customer
from account import BankAccount
from transaction import Transaction
import csv
import os


def save_customers_to_csv(bank_system, filename="customer.csv"):
    """Save all customers to a CSV file"""
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Customer_ID', 'Name', 'Email', 'Phone', 'Address', 'Account_Count', 'Total_Balance', 'Member_Since']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for customer_id, customer in bank_system.customers.items():
                writer.writerow({
                    'Customer_ID': customer.customer_id,
                    'Name': customer.name,
                    'Email': customer.email,
                    'Phone': customer.phone,
                    'Address': customer.address,
                    'Account_Count': customer.get_account_count(),
                    'Total_Balance': f"${customer.get_total_balance():.2f}",
                    'Member_Since': customer.created_date.strftime('%Y-%m-%d')
                })
        print(f"✓ Customers saved to {filename} successfully!")
    except Exception as e:
        print(f"✗ Error saving customers to CSV: {e}")


def save_transactions_to_txt(bank_system, filename="transaction.txt"):
    """Save all transactions to a TXT file"""
    try:
        with open(filename, 'w') as txtfile:
            txtfile.write("="*80 + "\n")
            txtfile.write("BANK TRANSACTION REPORT\n")
            txtfile.write("="*80 + "\n\n")
            
            if not bank_system.transactions:
                txtfile.write("No transactions found.\n")
            else:
                for transaction_id, transaction in bank_system.transactions.items():
                    txtfile.write(f"Transaction ID: {transaction.transaction_id}\n")
                    txtfile.write(f"Account Number: {transaction.account_number}\n")
                    txtfile.write(f"Type: {transaction.transaction_type}\n")
                    txtfile.write(f"Amount: {transaction.get_formatted_amount()}\n")
                    txtfile.write(f"Description: {transaction.description}\n")
                    txtfile.write(f"Date/Time: {transaction.date.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    if transaction.balance_after is not None:
                        txtfile.write(f"Balance After: ${transaction.balance_after:.2f}\n")
                    txtfile.write("-"*80 + "\n\n")
        
        print(f"✓ Transactions saved to {filename} successfully!")
    except Exception as e:
        print(f"✗ Error saving transactions to TXT: {e}")


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("WELCOME TO BANK MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add a New Customer")
    print("2. Add an Account to Customer")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Transfer Money")
    print("6. View Customer Information")
    print("7. View Account Information")
    print("8. View Transaction History")
    print("9. View System Summary")
    print("10. Save Customers to CSV")
    print("11. Save Transactions to TXT")
    print("12. Exit")
    print("="*50)


def add_customer(bank_system):
    """Add a new customer to the system"""
    print("\n--- ADD NEW CUSTOMER ---")
    name = input("Enter customer name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    
    customer_id = bank_system.add_customer(name, email, phone, address)
    print(f"✓ Customer added successfully! Customer ID: {customer_id}")


def add_account(bank_system):
    """Add a new account for a customer"""
    print("\n--- ADD NEW ACCOUNT ---")
    customer_id = input("Enter customer ID: ")
    
    if not bank_system.get_customer(customer_id):
        print("✗ Customer not found!")
        return
    
    print("Account types: checking, savings, business")
    account_type = input("Enter account type: ").lower()
    initial_balance = float(input("Enter initial balance: $"))
    
    try:
        account_number = bank_system.add_account(customer_id, account_type, initial_balance)
        print(f"✓ Account added successfully! Account Number: {account_number}")
    except ValueError as e:
        print(f"✗ Error: {e}")


def deposit_money(bank_system):
    """Process a deposit transaction"""
    print("\n--- DEPOSIT MONEY ---")
    account_number = input("Enter account number: ")
    
    if not bank_system.get_account(account_number):
        print("✗ Account not found!")
        return
    
    amount = float(input("Enter deposit amount: $"))
    
    try:
        transaction_id = bank_system.process_deposit(account_number, amount)
        if transaction_id:
            account = bank_system.get_account(account_number)
            print(f"✓ Deposit successful!")
            print(f"Transaction ID: {transaction_id}")
            print(f"New Balance: ${account.balance:.2f}")
        else:
            print("✗ Deposit failed!")
    except ValueError as e:
        print(f"✗ Error: {e}")


def withdraw_money(bank_system):
    """Process a withdrawal transaction"""
    print("\n--- WITHDRAW MONEY ---")
    account_number = input("Enter account number: ")
    
    account = bank_system.get_account(account_number)
    if not account:
        print("✗ Account not found!")
        return
    
    amount = float(input("Enter withdrawal amount: $"))
    
    try:
        transaction_id = bank_system.process_withdrawal(account_number, amount)
        if transaction_id:
            print(f"✓ Withdrawal successful!")
            print(f"Transaction ID: {transaction_id}")
            print(f"New Balance: ${account.balance:.2f}")
        else:
            print("✗ Insufficient funds!")
    except ValueError as e:
        print(f"✗ Error: {e}")


def transfer_money(bank_system):
    """Process a transfer between accounts"""
    print("\n--- TRANSFER MONEY ---")
    from_account = input("Enter source account number: ")
    to_account = input("Enter destination account number: ")
    amount = float(input("Enter transfer amount: $"))
    
    try:
        result = bank_system.process_transfer(from_account, to_account, amount)
        if result:
            trans_id1, trans_id2 = result
            from_acc = bank_system.get_account(from_account)
            to_acc = bank_system.get_account(to_account)
            print(f"✓ Transfer successful!")
            print(f"From Account Balance: ${from_acc.balance:.2f}")
            print(f"To Account Balance: ${to_acc.balance:.2f}")
        else:
            print("✗ Transfer failed (insufficient funds)!")
    except ValueError as e:
        print(f"✗ Error: {e}")

def view_customer_info(bank_system):
    """View customer information"""
    print("\n--- VIEW CUSTOMER INFORMATION ---")
    customer_id = input("Enter customer ID: ")
    
    customer = bank_system.get_customer(customer_id)
    if not customer:
        print("✗ Customer not found!")
        return
    
    print()
    customer.display_customer_info()
def view_account_info(bank_system):
    """View account information"""
    print("\n--- VIEW ACCOUNT INFORMATION ---")
    account_number = input("Enter account number: ")
    
    account = bank_system.get_account(account_number)
    if not account:
        print("✗ Account not found!")
        return
    
    print()
    account.display_account_info()


def view_transaction_history(bank_system):
    """View transaction history for an account"""
    print("\n--- VIEW TRANSACTION HISTORY ---")
    account_number = input("Enter account number: ")
    
    account = bank_system.get_account(account_number)
    if not account:
        print("✗ Account not found!")
        return
    
    transactions = bank_system.get_account_transactions(account_number)
    if not transactions:
        print("No transactions found for this account.")
        return
    
    print(f"\nTransaction History for {account_number}:")
    print("-" * 70)
    for trans in transactions:
        print(f"ID: {trans.transaction_id}")
        print(f"  Type: {trans.transaction_type} | Amount: {trans.get_formatted_amount()}")
        print(f"  Date: {trans.date.strftime('%Y-%m-%d %H:%M:%S')} | Balance: ${trans.balance_after:.2f}")
        print()


def view_system_summary(bank_system):
    """View overall system summary"""
    print("\n--- SYSTEM SUMMARY ---")
    summary = bank_system.get_system_summary()
    print(f"Total Customers: {summary['total_customers']}")
    print(f"Total Accounts: {summary['total_accounts']}")
    print(f"Total Transactions: {summary['total_transactions']}")
    print(f"Total System Balance: ${summary['total_balance']:.2f}")


def main():
    """Main function to run the bank system"""
    bank_system = BankSystem()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        
        try:
            if choice == "1":
                add_customer(bank_system)
            elif choice == "2":
                add_account(bank_system)
            elif choice == "3":
                deposit_money(bank_system)
            elif choice == "4":
                withdraw_money(bank_system)
            elif choice == "5":
                transfer_money(bank_system)
            elif choice == "6":
                view_customer_info(bank_system)
            elif choice == "7":
                view_account_info(bank_system)
            elif choice == "8":
                view_transaction_history(bank_system)
            elif choice == "9":
                view_system_summary(bank_system)
            elif choice == "10":
                save_customers_to_csv(bank_system)
            elif choice == "11":
                save_transactions_to_txt(bank_system)
            elif choice == "12":
                print("\nThank you for using Bank Management System. Goodbye!")
                break
            else:
                print("✗ Invalid choice! Please try again.")
        except ValueError:
            print("✗ Invalid input! Please enter valid data.")
        except Exception as e:
            print(f"✗ An error occurred: {e}")


if __name__ == "__main__":
    main()
