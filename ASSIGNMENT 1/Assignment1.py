'''QUESTION 1'''

import datetime #importing the datetime allowed which will be used later in the code.

def read_csv(file_path):
    data = [] #initializinf the data list to be empty at first
    with open(file_path, 'r') as file: #openign the file in read mode
        header = file.readline().strip().split(',') #this first part is reading the main header in the file and stripping all leading and trailing whitespaces while splitting based on the comma to extract necessary values from the file.It makes sense to split based on the comma as the files are comma separated value files.
        for line in file: #iterating for every linr in ythe file
            values = line.strip().split(',') #get the corresponding values in the file again by sptripping whitespaces and splitting based on the comma
            data.append(dict(zip(header, values))) #this now creates a list of dictionaries where each dictionary is a row in the file and the keys of the dictionaries are col names.The zip function is used here  to combine the header which is the col names also being the key s and the values which are the values on a row in the file.
    return data #returning the list of dictionaries.

def process_sales(sales_data, returns_data): #taking the 2 lists of sales_data and returns_data read from the respective files a sparameters for processing
    sales_with_returns = [] #Initializing the sakes with returns initially which will late rbe accounted for
    for sale in sales_data: #iterting through each sale
        sale_date = datetime.datetime.strptime(sale['date'], '%Y-%m-%d') #converting the sale date into a datetime object, this will help me in comparison of the dates

        for return_entry in returns_data: #for every return in returns_data
            return_date = datetime.datetime.strptime(return_entry['date'], '%Y-%m-%d') #again registering the return date in a datetime bject for comaprison purpsoses
            if sale['transaction_id'] == return_entry['transaction_id'] and sale_date <= return_date: #checks if the return has the same transaction ID as the sale and if the return is on or after the sale date as it doesn't logically make sense to return a product before its bought.
                sale['quantity'] = 0  # Marking the quantity as 0 for returned items, implying the sale is reversed and no quantity of the goods were sold
        sales_with_returns.append(sale) #append that sale to the sale_with returns list
    return sales_with_returns #returning the list


def calculate_total_units_sold(sales_data):
    total_units_sold = {} #Initializing he dict of tot_units sold as we will use this dict to store the product_id meaning the product and its corresponding sales
    for sale in sales_data: #for every sale in sales data
        product_id = sale['product_id'] #extracting the product_id from the sale
        quantity = int(sale['quantity']) #extracting the quantity from the sale
        total_units_sold[product_id] = total_units_sold.get(product_id, 0) + quantity # FIRST,This line is getting the value associated with the total units sold by using the product_id as the key and returning th edefault value 0 if no units wer sold which is the second parameter and storing this total_units_sold.
    return total_units_sold

def get_top_products(total_units_sold, products_data, n=3):  #this line is defining the get_top_products function that is taking 3 paramets, which are total_inits_Sold, the products_data and the additional parameter n=3 representing the number of products we need to display
    top_products = sorted(total_units_sold.items(), key=lambda x: x[1], reverse=True)[:n] #the total_units_sold.items() converts the dictionary into a list of tuples where each tuple contains a product_id along with the coressponding numbe rof units sold. the sorted and key=landa is actually sorting the list of tuples based on the second element ([1]) which is the total units sold in descending order. the key parameter specifies the lambda function which is extracting the second element. The :n selects the top n items from the sorted list and we know from the parameter that n=3 hence picking the top 3 vlaues from the sorted list.
    return [(products_data[product_id]['Product_Name'], units_sold) for product_id, units_sold in top_products] # here we are iterating over the top 3 productsand accessong the product_name with the gicven product_id  in the products_Data dict to get the name of product which is to be displayed 

# Read data from CSV files
products_data = {entry['Product_ID']: entry for entry in read_csv('transactions_Products.csv')[0:]} #Creating a dictionary products_data where the keys are product_ID values from the csv file and the values are the entire entries from the csv for each product.
sales_data = read_csv('transactions_Sales.csv')[0:] # the 0 slice is used to create the new list of dictionaries while indexing from the first eleement index=0 to the end,that therefore helps to make the list of dictionaries from the first entry to the last.
returns_data = read_csv('transactions_Returns.csv')[0:]


sales_with_returns = process_sales(sales_data, returns_data) #this line calls the process_sales function with the 2 parameters, it modifies the sales/_data by marking the quantity as 0 for any returned items, this data will then be later restored in the sales_with_returns variable.

# Calculating total units sold for each product based on the modifies sales data which is data after considering returns and returns a dictionary total_iunits_Sold where product IDs are keys and values are the total units sold for each product.
total_units_sold = calculate_total_units_sold(sales_with_returns) #

# Get the top 3 products
top_products = get_top_products(total_units_sold, products_data) #fucntion call with 2 parameters
print("QUESTION 1 OUTPUT")
# printing the results by looping through each tupke in the top_products listand for each iteration, it unpacks the tuple into the name and units_sold separately.the the alignment is done with a width of 20 chars and there is a justified right alignment with a width of 3 chars.
for product_name, units_sold in top_products:
    print(f"{product_name: >20} {units_sold: >3}")


#QUESTION 2


def process_sales_value(sales_data, returns_data): 
    sales_with_returns = [] #Initializing an empty list which will store the dales data with adjusted amount sfor returned items.
    for sale in sales_data:
        sale_date = datetime.datetime.strptime(sale['date'], '%Y-%m-%d') #this line converts the sale date from the file provided string format to a datetime object,this % indicates the expected date sring format.
        for return_entry in returns_data:
            return_date = datetime.datetime.strptime(return_entry['date'], '%Y-%m-%d') #same for return date
            if sale['transaction_id'] == return_entry['transaction_id'] and sale_date <= return_date: #same 2 conditions are checked as previous dfunctions for returns
                sale['amount'] = 0  # marking amount as 0 for returned items proving that no sale income was realized from returned sales
        sales_with_returns.append(sale) #appending this returned sale to the list
    return sales_with_returns

def calculate_total_sales_amount(sales_data, products_data):
    total_sales_amount = {} #Initializes an empty dict that will store the toal sales amount for each product
    for sale in sales_data:
        product_id = sale['product_id'] #extracts the product id from the current sale
        quantity = int(sale['quantity'])#extracts the quantity from the current sale
        #print(product_id)
        # Adjusting the product_id format because I was facing a lot of issues with the product_id not being picked entirely, this line helped to solve that problem
        product_id_adjusted = product_id  

        price_per_unit = float(products_data[product_id_adjusted]['Price']) #this retrieves the price per unit for the current product_id from tjhe products_data dictionary that we defined earlier, this price is then converted to a float.
        sale['amount'] = quantity * price_per_unit #calculating thr sale amount for the current sale by multiplying the quantity and the price per unit., the result will be stored in sale under the amount header.
        total_sales_amount[product_id_adjusted] = total_sales_amount.get(product_id_adjusted, 0) + sale['amount'] #this line is updating the total_sales_amount dict with the sale amount for the current product id, if tjhe product id is not already in the dictionary then it sets the initial value to 0 and adds the sales amount after that
    return total_sales_amount

def get_top_products_by_sales(total_sales_amount, products_data, n=3): #same fucntion as for units with minor tweaks to account for amount instead of units
    top_products = sorted(total_sales_amount.items(), key=lambda x: x[1], reverse=True)[:n]
    return [(products_data[product_id]['Product_Name'], amount) for product_id, amount in top_products]

'''calling the same 3 fucntions just like units, but now in the context of amount'''
# Process sales data considering returns
sales_with_returns = process_sales_value(sales_data, returns_data)

# Calculate total sales amount for each product
total_sales_amount = calculate_total_sales_amount(sales_with_returns, products_data)

# Get the top 3 products by sales amount
top_products_by_sales = get_top_products_by_sales(total_sales_amount, products_data)
print("QUESTION 2 OUTPUT")
# Printing the results as per the alignment guideline sprivided in the question
for product_name, amount in top_products_by_sales:
    formatted_amount = "${:,.2f}".format(amount)
    print(f"{product_name: >20} {formatted_amount: >10}")




#QUESTION3


def process_sales_q3(sales_data, returns_data):
    sales_with_returns = [] #reiterating the same idea from previous functions of sales_with_returns
    for sale in sales_data: #for every sale in sale_data
        sale_date = datetime.datetime.strptime(sale['date'], '%Y-%m-%d') #
        for return_entry in returns_data: #for every entry in the returns_data list  
            return_date = datetime.datetime.strptime(return_entry['date'], '%Y-%m-%d') #using the same logic as the sale_date
            if sale['transaction_id'] == return_entry['transaction_id'] and sale_date <= return_date:
                sale['quantity'] = 0  # Mark quantity as 0 for returned items this is becuase the quantity is 0 for any returned items
                sale['discount'] = 0  # Mark discount as 0 for returned items this is becuase the discount is 0 for any returned items
        sales_with_returns.append(sale) #append the returned sale to the sale_with_returns list
    return sales_with_returns

def calculate_product_statistics(sales_data, products_data): 
    product_statistics = {} #I'm initializng a disctionary that will store 
    for sale in sales_data: #for every sale in sale_data
        product_id = sale['product_id'] #extracting the product_id from the sale
        quantity = int(sale['quantity']) #extracting the quantity of sale from the sale dict and converting it to perform calculations on it
        price_per_unit = float(products_data[product_id]['Price']) # uses the product_id as key to extract the revelant price of the product from the products_data dict where price if the corresponding value
        discount_percentage = float(sale['discount']) * 100 #covnerting the decimal discount into a percentage
        discounted_amount = quantity * price_per_unit * ( float(sale['discount'])) #This is the amount of the discount portion out of the total sale value
        sale_amount = quantity * price_per_unit #the s=total sale_amount is bound to be sales*quantity
        product_name = products_data[product_id]['Product_Name'] #to extract he relevant product name, we extract the value of the product name from the products_Data dic tusing the product_id as the key

        if product_id not in product_statistics: #if the product_id is not in the product_Statistics dictionary , it means it was a return and once I know its a return I am going to nullify all relevant details, to create it as a blank record so it doesn't affect my calculated statistics.
            product_statistics[product_id] = {
                'product_name': product_name,
                'total_units_sold': 0,
                'total_sale_amount': 0,
                'total_discounted_amount': 0,
                'total_discount_given': 0
            }
        
        product_statistics[product_id]['total_units_sold'] += quantity #summing the total_units_sold with sale quantiy of current sale
        product_statistics[product_id]['total_sale_amount'] += sale_amount #summing the total_sale_amount with sale amount of current sale
        product_statistics[product_id]['total_discounted_amount'] += discounted_amount #summing the total_discounted_amount with sale discount amount of current sale
        product_statistics[product_id]['total_discount_given'] += discount_percentage #summing the total_discount_given with discount percentage of current sale
 
    return product_statistics #returning the product_Statistics dict
print("QUESTION 3 OUTPUT")
def print_turnover_table(product_statistics):
    # Printing table header as per the format with the respective columns and the formatting of the +'s for corners and |for borders
    print("+---+--------------------+---+---------------+--------+---------------+")
    print("|ID |Product Name        |Qty|Total Amount   |Avg Disc|Total Discount |")
    print("+---+--------------------+---+---------------+--------+---------------+")

    
    for product_id, stats in sorted(product_statistics.items(), key=lambda x: x[1]['total_discounted_amount'], reverse=True): #I'm starting a while loop here to iterate over the items in th eproduct_statistics dictionary and I will perform sorting of the items based on the total_discountedamount column
        print(f"|{product_id: >3}|{stats['product_name']: <20}|{stats['total_units_sold']: >3}|$ {stats['total_sale_amount']: >13,.2f}|{stats['total_discount_given'] / stats['total_units_sold']: >7.2f}%|${stats['total_discounted_amount']: >13,.2f}|") #Witihin the loop,I wish to print a formatted row for ewach productm the f-string is ised for the formatting with the respective formatting fucntions which I am using to align and format the values in each col

    # Printing the table footer
    print("+---+--------------------+---+---------------+--------+---------------+")

#calling the functions just like in previous functions


sales_with_returns = process_sales_q3(sales_data, returns_data)


product_statistics = calculate_product_statistics(sales_with_returns, products_data)


print_turnover_table(product_statistics)


#QUESTION 4
#if statement to check monday to be done

def count_transactions_per_weekday(sales_data):
    weekday_counts = {} #Initializing the weekday_counts dict which I will uise fto store the count of transactions per each weekday
    for sale in sales_data: #for every sale
        sale_date = datetime.datetime.strptime(sale['date'], '%Y-%m-%d') #I'm extracting the date attribute from each sale and converting it to a datetime object using the strp time method from the datetime modele.
        weekday = sale_date.strftime('%A') #Then I'mn extracting the weekday name from the datetime object using the strftime and the formatting of %A which is going to give me the full weekday name that I'm looking for.
        
        if weekday not in weekday_counts: #Iff a weekday key doesn't exist in weekday_counts then I'm going to add the weekday into the dictionary and give it the sale count of 0
            weekday_counts[weekday] = 0
        
        weekday_counts[weekday] += 1 #Incrementing the count for the specific weekday in the dict by 1 for each sale

    return weekday_counts

# Read data from CSV files
sales_data = read_csv('transactions_Sales.csv')[1:] #Readign the data from the transactions_sales csv and stating from 1 so that the header row can be skipped

# Counting transactions per weekday by calling the fucntiom
weekday_counts = count_transactions_per_weekday(sales_data)

# Printing the results
print("Monday   : 0") #hard-code for clarity
for weekday, count in weekday_counts.items(): #I'm iterating through the weekday_counts dict and printing each weekday aling with the coressponding count,  Also accounting for the formatting  via <9 and >3 to satisfy the requirements of the question
    print(f"{weekday: <9}:{count: >3}")

#QUESTION 5


def get_returned_products(return_data, products_data):
    returned_products = {} #Initializing the empty returned_products dict dict to store more info about the returned products
    for return_entry in return_data: #for every returned products entry in the treturn_Data dict
        transaction_id = return_entry['transaction_id'] #I'm exteracting the trasaction_id from each return entry and initiazlizing a varaliable product_id to none because the product_id for that transaction becomes null at this ppint.
        product_id = None

        for sale_entry in sales_data:
            if sale_entry['transaction_id'] == transaction_id:
                product_id = sale_entry['product_id']
                break #This bit of my code is now iterating through each entry in the sales_data list and checking if the transaction/_id mathces one from the return entry.If they do match then in that case it sets the product_id to the coreresponding_product_id from the sales data and then breaks out of the loop

        if product_id:
            product_name = products_data[product_id]['Product_Name']

            if product_id not in returned_products:
                returned_products[product_id] = {
                    'product_name': product_name,
                    'return_count': 0
                }
        #If a valid product_id is obdatined from the sales data, it extracts the product_name assicated with that product_id from the prodcuts_Data dict.After that, if the product_id is not already present in the returned_products dict, I add a new entry with the product_id as the key . The assocaited value is a dictionary with product_name and return_Count initialzied to the product name and 0 repsectively .
            
            returned_products[product_id]['return_count'] += 1 #Then I'm incrementing the return_count for that specific product in the returned_product dict.

    return returned_products #then returning all the returned_products data



# Get returned products
returned_products = get_returned_products(returns_data, products_data) #Callign the fucntion
print("QUESTION 5 OUTPUT")
#Regarding the printing, I am starting a lop that iterates through each item in the returned_products dictm each item is bound to have a product_id which is the kwey and the product_info which is the value .Then, inside the loop , I am extracting the product_name and the reurn_cpount from the product_info dict.
for product_id, product_info in returned_products.items():
    product_name = product_info['product_name']
    return_count = product_info['return_count']
    print(f"{product_id: <3} {product_name: <20} {return_count: >3}") #here I'm suing a formatted string for each returned product, <3 is for the purpose of width 3 left alignement and <20 if dfor left alignment for the product_name with a width of 20 while >3 for  the reutrn count is to be right_aligned with a width of 3

#QUESTION 6

print("QUESTION 6 OUTPUT IN FILE") 




sales_data = read_csv('transactions_Sales.csv')[1:] #Once again this line isreading my transacctions_sales csv and starting from 1 to skip the header row.

# Then I'm calling myt total_units_Sold function with the sales_Data
total_units_sold = calculate_total_units_sold(sales_data) 


with open('transactions_units.txt', 'w') as file:
    for product_id, units_sold in total_units_sold.items():
        file.write(f"{product_id},{units_sold}\n")
#Then I'm opening my transactions_units file for writing,and iterating through each item in the total_units_sold dictFor every iteration, I'm writing a line in the file which is formatted into a csv format with the product_id and the units_solf separated with a comma followed with the new line character to move onto the next line to record the next transactions entry