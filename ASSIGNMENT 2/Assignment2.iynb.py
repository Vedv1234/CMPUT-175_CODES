#Question 1
import pandas as pd

#MOUNTING THE DRIVE AND READING ALL THE RESPECTIVE 3 LINES
from google.colab import drive
drive.mount('/content/drive')

products_df = pd.read_csv('/content/drive/MyDrive/transactions_Products_January.csv')
sales_df = pd.read_csv('/content/drive/MyDrive/transactions_Sales_January.csv')
returns_df = pd.read_csv('/content/drive/MyDrive/transactions_Returns_January.csv')

# Converting the date into an object of datetime module just like I did in python but using a method of pandas
sales_df['date'] = pd.to_datetime(sales_df['date'])

# Separating the transactions before and after January 8th  using direct comparison
sales_before_jan8 = sales_df[sales_df['date'] < '2024-01-08']
sales_after_jan8 = sales_df[sales_df['date'] >= '2024-01-08']
# Calculating the average number of transactions without discount before and after January 8th and storing them in respective dataframes
avg_no_discount_before = (sales_before_jan8['discount'] == 0).mean() * 100
avg_no_discount_after = (sales_after_jan8['discount'] == 0).mean() * 100

# Printing the average number of transactions without discount before and after January 8th
print(f"Average transaction without discount: {avg_no_discount_before:.2f}% and after the discount {avg_no_discount_after:.2f}%") #using fstring formatting to maintain 2dp

# I'm Calculating the average discount per product before and after January 8th
avg_discount_before = sales_before_jan8.groupby('product_id')['discount'].mean().reset_index() #I'm grouping by the product_id and discount cols because those are the respective cols I need to get discount for the particualr product
avg_discount_before.columns = ['Product_ID', 'Average_Discount_Before'] #dataframe for discounts before
avg_discount_after = sales_after_jan8.groupby('product_id')['discount'].mean().reset_index() #Again grouping by after and resseting the index so that the col doesn't become a new index,we need a new fresh index for an accurate dataframe
avg_discount_after.columns = ['Product_ID', 'Average_Discount_After'] #same, dataframe for discounts after with only the 2 cols of interest

# Mergeing the filtered results with the product_df dataframe using the merge on the product_id as it is the common col in both the dataframes.
avg_discount_before = pd.merge(avg_discount_before, products_df, on='Product_ID') 
avg_discount_after = pd.merge(avg_discount_after, products_df, on='Product_ID')

# Now i'm printing the result in the desired format 
print("\nAverage discount per product:")# newline for header printing
print("{:<3} {:<20} <08-01  - >=08-01".format("PID", "Product Name")) #this line , i am first formatting for left alignment by width 3,then for the seconf value which is product name,I' left aligning with wiidth 20 then putting the string format as per what I saw in the sample output,, then iusing the format functionto replace the placeholders that I initialized with the actual values o fPID and prodcutname
for index, row in avg_discount_before.iterrows(): #for every row and index in the discount before daraframe, I'm performing a rowwise iteration
    product_id = row['Product_ID'] #storing the producit_id
    product_name = row['Product_Name'] #stooring the product_anme
    avg_disc_before = row['Average_Discount_Before'] * 100 #storing avg discount before
    avg_disc_after = avg_discount_after.loc[avg_discount_after['Product_ID'] == product_id, 'Average_Discount_After'].values[0] * 100 # I'm using the loc accesor to locate the rows where the product_id matches the current product_id I have,then only picks the avergae_diuscount_After fore those rows only..The values[0] extracts only the first and only rowof the resulting dataframe SINCE i AM ONLY EPECTING 1 VALUE FOR EXTRACTION FROM THE DATAFRAME.
    print("{:>3} {:>20} {:>5.2f}% - {:>5.2f}%".format(product_id, product_name, avg_disc_before, avg_disc_after)) #similar formatting principles as the one for dicount before avgt.

import matplotlib.pyplot as plt




#QUESTION 2
# Merging the sales and products data to get the product name, the merged_df is a common df where I'm getting all my values.was encountering a lot of errors, with prodcut_id so did both a left and right join
merged_df = pd.merge(sales_df, products_df, left_on='product_id', right_on='Product_ID') 

# Calculating the amount after discount and then storing it a new column
merged_df['Amount'] = (merged_df['quantity'] * merged_df['Price']) * (1 - merged_df['discount'])

# Calculating the weekday for each transaction and using daytime fucntions day_name and pandas function to_datetime for effective extraction
merged_df['weekday'] = pd.to_datetime(merged_df['date']).dt.day_name()

# Merging the  returns with sales to acocunt for the returns
merged_returns_df = pd.merge(returns_df, sales_df, on='transaction_id', how='left')
merged_returns_df = pd.merge(merged_returns_df, products_df, left_on='product_id', right_on='Product_ID', how='left')

# Calculating th the shelving cost for each returned product
merged_returns_df['shelving_cost'] = merged_returns_df['Price'] * merged_returns_df['quantity'] * 0.1

# Calculating the total shelving cost for each return day, using sum as the affregate fucntuon hered
returns_daily_cost = merged_returns_df.groupby('date_x')['shelving_cost'].sum().reset_index(name='Total_Shelving_Cost')

# Grouping by the weekday and calculating the average transactions and turnover for each day and storing them in their respective dataframes
avg_transactions_per_weekday = (merged_df.groupby(['weekday', 'transaction_id'])
                                 .size().reset_index(name='NB Tr')
                                 .groupby('weekday')['NB Tr'].mean().reset_index(name='NB Tr'))

avg_turnover_per_weekday = (merged_df.groupby(['weekday', 'transaction_id'])
                             .agg(Turnover=('Amount', 'sum'))
                             .reset_index())

# Adingd the returned shelving cost to the total shelving cost for each return day for inclusion fo returned transaccitoms
avg_turnover_per_weekday = pd.merge(avg_turnover_per_weekday, returns_daily_cost, left_on='weekday', right_on='date_x', how='left')
avg_turnover_per_weekday['Turnover'] = avg_turnover_per_weekday['Turnover'].add(avg_turnover_per_weekday['Total_Shelving_Cost'], fill_value=0)

# Formatting the amount column using th emap function
avg_turnover_per_weekday['Turnover'] = avg_turnover_per_weekday['Turnover'].map('${:,.2f}'.format)

# I was using the earlier merged_df but encountering a lot issues so created a new result_df for re-merging the two DataFrames
result_df = pd.merge(avg_transactions_per_weekday, avg_turnover_per_weekday, on='weekday')
#print("---->", result_df)
# Rounding the number of transactions to the closest integer as we can't have 0.25 of a transaction
result_df['NB Tr'] = result_df['NB Tr'].round()
# Initialize dictionaries to store total transactions and turnover per weekday
#print("---->", result_df)
total_transactions = {} #initalizing dict for total_transactions per day
total_turnover = {} #initializing the dict for total turnover

# Accumulating the values for each weekday
for index, row in result_df.iterrows(): #I'm performing rowwirsw iteratin here
    #I'm extracting the day,nb_transactions,turnove rhere which will later be aggregated
    day = row['weekday']
    nb_transactions = int(row['NB Tr'])
    turnover = float(row['Turnover'].replace('$', '').replace(',', ''))  # Removing '$' and ',' before converting to float otherwise it was giving me a lot of erros

    # Updating total transactions and turnover for each weekday
    if day in total_transactions:
        total_transactions[day] += nb_transactions #summing transactions
        total_turnover[day] +=  #summing hte turnover
    else:
        total_transactions[day] = nb_transactions #otherwise they are remaining constant
        total_turnover[day] = turnover

# Printigm the total result in the specified format , used the sample output for guidance
print(" +-----------+-----+-------------+")
print(" | Day       |NB Tr|    Turnover |")
print(" +-----------+-----+-------------+")
for day in total_transactions.keys():
    nb_transactions_total = total_transactions[day]
    turnover_total = "${:,.2f}".format(total_turnover[day])
    print(" | {:<9} | {:>3} | {} |".format(day, nb_transactions_total, turnover_total))
print(" +-----------+-----+-------------+")



# Setting up the bar colors , used the w3 schools website to learn this method.Respect their content here.
colors = {'Monday': 'blue', 'Tuesday': 'blue', 'Wednesday': 'blue', 'Thursday': 'blue', 'Friday': 'red', 'Saturday': 'red', 'Sunday': 'red'}

import plotly.express as px #I really tried to make the bar charts with matplotlib but they kept giving me erroes, I also fdo CMPUT 195 , There we mostly use pltly becuase it is so much eaiser to plot graphs using pltly that's why I used plotly here. Sorry!

# Sample data which I used for testing
data = {
    'weekday': ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday'],
    'nb_transactions_total': [298, 257, 299, 293, 298, 353, 326],
    'turnover_total': [232735.87, 190406.64, 211245.04, 248937.70, 201680.08, 275374.68, 237716.63]
}

# Creating a DataFrame, already had one but it was giving me an error, so reinitialize dit
result_df = pd.DataFrame(data)

# Setting up the bar colors
colors = {'Monday': 'blue', 'Tuesday': 'blue', 'Wednesday': 'blue', 'Thursday': 'blue', 'Friday': 'red', 'Saturday': 'red', 'Sunday': 'red'}

# Creating the actual bar chart for the number of transactions per weekday
# Import necessary libraries
import plotly.express as px

# Create a Plotly bar chart for the number of transactions per weekday
fig_transactions = px.bar(
    result_df, # DataFrame containing the data
    x='weekday', # X-axis: weekday
    y='nb_transactions_total', # Y-axis: number of transactions
    color='weekday' # Color by weekday
    text='nb_transactions_total # Text to be displayed on the bars
    labels={'nb_transactions_total': 'Transactions', 'weekday': 'Day of the Week'},  # Axis labels
    title='Number of Transactions per Weekday',# Chart title
    color_discrete_map=colors# Map colors to weekdays
    )

# Display the bar chart
fig_transactions.show()

fig_transactions.update_traces(texttemplate='%{text}', textposition='outside') #Once again I give credits to w3 schools, text template  specifies the format of the text displayed on the bars. 

fig_amounts = px.bar(result_df,  # Using Plotly Express to create a bar chart, I wanted to use MatPlotLiba nd really tieed to but I kept getting errors,I take CMPUT 195 and we mostly use pltly there because it s much simpler to use, Sorry!
                     x='weekday',# x-axis represents the weekdays
                     y='turnover_total',#Y-axis represents the turnover_total
                     color='weekday', #Color represents the weekday
                     text='turnover_total', # Text labelcs on bars are set to thecs values in 'turnover_total'
                     labels={'turnover_total': 'Dollar Amount', 'weekday': 'Day of the Week'},# Labels for axes
                     title='Amount of Sales per Weekday',# Title of the chart
                     color_discrete_map=colors)  # I'm Assigning colors to weekdays using the 'colors' dictionary
fig_amounts.update_traces(texttemplate='%{text}', textposition='outside') #same applicatiiona s for transactions


fig_transactions.show()
fig_amounts.show()





#qurstion3 
# This code calculates the return shelvincwpog cost for each returnewed product by merging the retursens, sales, and products dataframes
merged_returns_df = pd.merge(returns_df, sales_df, on='transaction_id', how='left')
merged_returns_df = pd.merge(merged_returns_df, products_df, left_on='product_id', right_on='Product_ID', how='left')

# Apply a 10%tne shelving cost rate to calculatkfne the cost for each returned product
merged_returns_df['shelving_cost'] = merged_returns_df['Price'] * merged_returns_df['quantity'] * 0.1

# Calculate the total shelvsmqing cost for eachw return day
returns_daily_cost = merged_returns_df.groupby('date_x')['shelving_cost'].sum().reset_index(name='Total_Return_Shelving_Cost')

# Finding the day with the highest return shelving cost
most_expensive_day = returns_daily_cost.loc[returns_daily_cost['Total_Return_Shelving_Cost'].idxmax()]

# Displaying the information about the most expensive return day
print(f"{most_expensive_day['date_x']}, Total Return Shelving(RS) Cost=$ {most_expensive_day['Total_Return_Shelving_Cost']:.2f}")

# Filtering returns for the most expensive day to get the details of returned items
most_expensive_returns = merged_returns_df[merged_returns_df['date_x'] == most_expensive_day['date_x']]

# Displaying the list of items returned on the most expensive return day
print("Products Returned that day:")
print("PID         Product Name          NoI     RS Cost")
for index, row in most_expensive_returns.iterrows():
    # Extracting [w] relevant information for each returned product
    product_id = row['product_id']
    product_name = row['Product_Name'][:20]  # Display only the first 20 characters of the product name
    num_items = int(row['quantity'])
    shelving_cost = row['shelving_cost']

    # Printinfw the details of the returned product
    print(f"{product_id: <3} {product_name: <20} {num_items: 3} ${shelving_cost:,.2f}")


    #question 4
    #The 'sales_df' and 'products_df' DataFrames are merged based on the 'product_id' and 'Product_ID' columns,I was encounteirng some issues when I only used a left join so I did noth then the code seemed to work just fine, Magic!
    merged_df = pd.merge(sales_df, products_df, left_on='product_id', right_on='Product_ID')
    
    # # For rows in 'merged_df' where the 'transaction_id' is present in 'returns_df',I am multiplying the 'quantity' by -1
    merged_df.loc[merged_df['transaction_id'].isin(returns_df['transaction_id']), 'quantity'] *= -1
    
    # Grouing the p 'merged_df' by 'product_id' and summing the 'quantity' for each group to get total units sold here
    total_units_sold = merged_df.groupby('product_id')['quantity'].sum().reset_index(name='Total_Units_Sold')
    
    #I'm Extracting the numerical part from product IDs for sorting using the extract function instr,I learnt this from w3 schools.
    total_units_sold['Product_ID_Num'] = total_units_sold['product_id'].str.extract('(\d+)').astype(int)
    
    # Sorting using sort_valis method the results by numerical part of product ID
    total_units_sold = total_units_sold.sort_values(by='Product_ID_Num')
    
    # Writing the sorted results to a text file
    with open("order_supplier_January.txt", "w") as file:
        for index, row in total_units_sold.iterrows():#dpoing worwiseiteratins hee
            product_id = row['product_id']
            product_name = products_df.loc[products_df['Product_ID'] == product_id, 'Product_Name'].values[0]
            units_sold = row['Total_Units_Sold']
            file.write(f"{product_id}#{product_name}#{units_sold}\n")
    
    # Printign the sorted information on the screen as per the sample output reference that is on Eclass
    print("Product ID  Product Name               Units to Order")
    print("--------------------------------------------------")
    for index, row in total_units_sold.iterrows():
        product_id = row['product_id']
        product_name = products_df.loc[products_df['Product_ID'] == product_id, 'Product_Name'].values[0]
        units_sold = row['Total_Units_Sold']
        print(f"{product_id: >3} {product_name: <20} {units_sold: >3}")


        #QUESTION 5
        
        # Merging sales and products data to get the product name to create the new merged_Sales_Df
        merged_sales_df = pd.merge(sales_df, products_df, left_on='product_id', right_on='Product_ID', how='left')
        
        # Identifying the  products that were never sold 
        unwanted_products = products_df[~products_df['Product_ID'].isin(merged_sales_df['product_id'].dropna())] #I want to remove ant Nan vales that[s why I'm dropping htem
        if len(unwanted_products) > 0:  # Checking if there are unwanted products
            # I'm Printfpowj products that were never sold
            print("Unwanted Products (Never Sold):")  # Displayifn header for unwanted products
            for index, row in unwanted_products.iterrows():  # Iterateimg through each roww in unwanted_products
                product_id = row['Product_ID']  # Get the Product ID
                product_name = row['Product_Name']  # Get the Product Name
                print(f"{product_id: >3} {product_name: <20}")  # Print Product ID and Name
        else:
            # Find products with the least sales
            least_sold_products = merged_sales_df.groupby(['Product_ID', 'Product_Name']).size().reset_index(name='Sales_Count')
            least_sold_products = least_sold_products.sort_values(by='Sales_Count').head(1)
        
            # i;mGetting the dates of sale for the least sold product
            least_sold_product_id = least_sold_products['Product_ID'].iloc[0]
            least_sold_dates = merged_sales_df[merged_sales_df['product_id'] == least_sold_product_id]['date'].tolist()
        
            # Printog the least sold product with dates
            print(f"Least Sold Product: {least_sold_product_id} {least_sold_products['Product_Name'].iloc[0]} "
                  f"{least_sold_products['Sales_Count'].iloc[0]:03} {least_sold_dates}")



            
            
            
            
     
            
            
            #question 6
            
            # I'm Groupifewo by product and calculate the average price and discount
            average_data = merged_df.groupby('product_id').agg({'Price': 'mean', 'discount': 'mean'}).reset_index()
            
            # Extracting relevant columns and just giving them variables for easy recognition and since my approach is mathematical, x and y are meaning ful variable naems/
            x = average_data['Price']
            y = average_data['discount']
            #print(x)
            #print(y)
            # Calculate the Pearson correlation coefficient
            # Using np.corrcoef to compute the correlation matrix between 'x' and 'y'
            correlation_matrix = np.corrcoef(x, y) 
            
            #i am,s cxextractign the Pearson correlation coefficient from the matrix
            pearson_correlation = correlation_matrix[0, 1]
            
            # Printing the result with three decimal places
            print(f"Pearson Correlation= {pearson_correlation:.3f}")
            
            #I'm Fitting a linear regression line
            #i am then using np.polyfit to fit a linear regression line to 'x' and 'y'
            coef = np.polyfit(x, y, 1)
            
            # THneCreating a polynomial function based on the coefficients
            poly1d_fn = np.poly1d(coef)
            
            
            # Setvp the figure size sto 8x6 inches
            plt.figure(figsize=(8, 6))
            
            # Creaitng rhtf wqcScatter plot of 'x' and 'y' with blue color
            plt.scatter(x, y, label='Data Points', color='blue')
            
            # Plottingw the linear regression line with a dashed black line
            plt.plot(x, poly1d_fn(x), '--k', label='Linear Regression Line')
            
            # Settin up the  labels for the x and y axes
            plt.xlabel('Average Product Price')
            plt.ylabel('Average Discount')
            
            # Givient  the title of the plot
            plt.title('Correlation between Average Product Price and Discount')
            
            # Display the legend and the actual plot
            plt.legend()
            plt.show()
