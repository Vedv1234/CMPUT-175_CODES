import csv
from collections import defaultdict

# Function to read CSV file and return data as a list of dictionaries
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Function to convert string to float or return 0.0 if not possible
def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return 0.0

# Function to calculate total units sold for each product
def calculate_units_sold(sales_data, returns_data):
    units_sold = defaultdict(int)
    for sale in sales_data:
        product_id = sale['product_id']
        quantity = int(sale['quantity'])
        units_sold[product_id] += quantity

    # Adjust units sold based on returns
    for return_data in returns_data:
        returned_transaction_id = return_data['transaction_id']
        if returned_transaction_id in units_sold:
            units_sold[returned_transaction_id] = 0

    return units_sold

# Function to calculate total sales in dollars for each product
from collections import defaultdict

# Function to calculate total sales in dollars for each product
from collections import defaultdict

from collections import defaultdict

# Function to calculate total sales in dollars for each product
def calculate_sales(products_data, sales_data, returns_data):
    products_dict = {product['Product_ID']: product for product in products_data}
    sales_in_dollars = defaultdict(float)
    for sale in sales_data:
        product_id = sale['product_id']
        quantity = int(sale['quantity'])
        discount = float(sale['discount'])

        # Skip entries with non-numeric price
        price_per_unit = safe_float(products_dict.get(product_id, {}).get('Price', 0.0))

        total_price = quantity * price_per_unit * (1 - discount)
        sales_in_dollars[product_id] += total_price

    # Adjust sales based on returns
    for return_data in returns_data:
        returned_transaction_id = return_data['transaction_id']
        if returned_transaction_id in sales_in_dollars:
            sales_in_dollars[returned_transaction_id] = 0

    return sales_in_dollars



def get_top_products(total_sales, products_data, n=3):
    # Convert total_sales dictionary to a list of tuples (product_id, total_amount)
    sales_list = list(total_sales.items())
    
    # Sort the list by total amount in descending order
    sorted_sales = sorted(sales_list, key=lambda x: x[1], reverse=True)[:n]

    # Extract product information (name and amount) for the top products
    top_products_info = [(product_info['Product_Name'], total_amount) 
                         for product_id, total_amount in sorted_sales 
                         if (product_info := next((product for product in products_data if product['Product_ID'] == product_id), None)) is not None]

    return top_products_info


# Function to write total units sold to a text file
def write_units_to_file(units_sold, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for product_id, units in units_sold.items():
            output_file.write(f"{product_id},{units}\n")

# Read data from CSV files
products_data = read_csv("transactions_Products.csv")
sales_data = read_csv("transactions_Sales.csv")
returns_data = read_csv("transactions_Returns.csv")

# Calculate total units sold
units_sold = calculate_units_sold(sales_data, returns_data)

# Write total units sold to the text file
output_file_path = "transactions_units.txt"
write_units_to_file(units_sold, output_file_path)

# Calculate total sales in dollars
total_sales = calculate_sales(products_data, sales_data, returns_data)

# Display the top 3 products with the largest sales in dollars
print("\nTop 3 Products with Largest Sales in Dollars:")
sorted_sales = sorted(total_sales.items(), key=lambda x: x[1], reverse=True)[:3]
products_dict={}
for product_id, total_amount in sorted_sales:
    product_info = products_dict.get(product_id, {})
    product_name = product_info.get('Product_Name', "")
    formatted_amount = f"${total_amount:,.2f}"
    print(f"{product_name: <20} {formatted_amount: >10}")