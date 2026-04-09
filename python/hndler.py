import csv
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_CUSTOMER_CSV = ROOT_DIR / 'customer.csv'

CSV_FIELDS = [
    'Customer_ID',
    'Name',
    'Email',
    'Phone',
    'Address',
    'Account_Count',
    'Total_Balance',
    'Member_Since',
]


def save_customers_to_csv(customers, filename=None):
    '''Save customer records to customer.csv.'''
    if filename is None:
        filename = DEFAULT_CUSTOMER_CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for customer in customers:
            writer.writerow({
                'Customer_ID': customer['Customer_ID'],
                'Name': customer['Name'],
                'Email': customer['Email'],
                'Phone': customer['Phone'],
                'Address': customer['Address'],
                'Account_Count': customer.get('Account_Count', 0),
                'Total_Balance': customer.get('Total_Balance', 0.0),
                'Member_Since': customer.get('Member_Since', datetime.now().strftime('%Y-%m-%d')),
            })


def load_customers_from_csv(filename=None):
    '''Load customer records from customer.csv.'''
    if filename is None:
        filename = DEFAULT_CUSTOMER_CSV
    customers = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Account_Count'] = int(row['Account_Count']) if row['Account_Count'] else 0
            row['Total_Balance'] = float(row['Total_Balance'].replace('$', '').strip()) if row['Total_Balance'] else 0.0
            customers.append(row)
    return customers


def sample_customers():
    '''Return sample customer entries for customer.csv.'''
    return [
        {
            'Customer_ID': 'CUST0001',
            'Name': 'Alice Johnson',
            'Email': 'alice.johnson@example.com',
            'Phone': '+1-555-0123',
            'Address': '123 Maple Street, Townsville',
            'Account_Count': 2,
            'Total_Balance': 4520.75,
            'Member_Since': '2024-01-15',
        },
        {
            'Customer_ID': 'CUST0002',
            'Name': 'Brian Lee',
            'Email': 'brian.lee@example.com',
            'Phone': '+1-555-0456',
            'Address': '456 Oak Avenue, Cityburg',
            'Account_Count': 1,
            'Total_Balance': 1360.50,
            'Member_Since': '2024-03-02',
        },
        {
            'Customer_ID': 'CUST0003',
            'Name': 'Carmen Patel',
            'Email': 'carmen.patel@example.com',
            'Phone': '+1-555-0789',
            'Address': '789 Pine Road, Villageton',
            'Account_Count': 3,
            'Total_Balance': 9240.00,
            'Member_Since': '2023-11-22',
        },
    ]


if __name__ == '__main__':
    customers = sample_customers()
    save_customers_to_csv(customers)
    print(f'Saved {len(customers)} rows to customer.csv')
