# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=duplicate-code
# pylint: disable=unused-variable



import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# import numpy as np

# Read in the data
df = pd.read_csv('data/transactions.csv')

# print out the data
# print(df)

# add the 'Amount' column to amount_sum if the "Transaction Type" is "credit"
def calc_account_balance():
    account_balance = 0
    for index, row in df.iterrows():
        if row['Transaction Type'] == 'credit':
            account_balance += row['Amount']
        if row['Transaction Type'] == 'debit':
            account_balance -= row['Amount']
    return account_balance

def unique_categories():
    return df['Category'].unique()

# Returns Dictionary of categories and their total spending
def tally_categories():
    tally = {}
    for index, row in df.iterrows():
        if row['Category'] in tally:
            #category already exists
            if row['Transaction Type'] == 'credit':
                #credit
                tally[row['Category']] += row['Amount']
            else:
                #debit
                tally[row['Category']] -= row['Amount']
        else:
            #create new category
            tally[row['Category']] = row['Amount']
    del tally['Transfer']
    return tally

def plot_histogram():
    x = []
    y = []
    for key, value in tally_categories().items():
        x.append(key)
        y.append(value)
    fig = plt.figure(figsize = (20, 10))
    plt.bar(x, y, color ='maroon', width = 1.0)
    plt.xticks(rotation=30, ha='right')

    plt.xlabel("Categories")
    plt.ylabel("Amount spent")
    plt.title("Amount spent on each category")
    plt.savefig("Amount Spent.png")

def calc_food_spending():
    tally = tally_categories()
    food_spending = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Restaurants' or key == 'Groceries' or key == 'Food & Dining':
            food_spending += tally.get(key)
        if key == 'Food Delivery' or key == 'Fast Food' or key == 'Coffee Shops':
            food_spending += tally.get(key)
    return food_spending


def calc_housing_spending():
    tally = tally_categories()
    housing_spending = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Mortgage & Rent':
            housing_spending += tally.get(key)
    return housing_spending

def calc_transportationtravel_spending():
    tally = tally_categories()
    transportation_spending = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Ride Share' or key == 'Travel' or key == 'Gas & Fuel':
            transportation_spending += tally.get(key)
        if key == 'Parking' or key == 'Air Travel' or key == 'Rental Car & Taxi':
            transportation_spending += tally.get(key)
        if key == 'Hotel':
            transportation_spending += tally.get(key)
    return transportation_spending

def calc_medical_spending():
    tally = tally_categories()
    med_spending = 0

    keys = tally.keys()
    for key in keys:
        if key == 'Dentist' or key == 'Doctor' or key == 'Pharmacy':
            med_spending += tally.get(key)
    return med_spending


def calc_utilities_spending():
    tally = tally_categories()
    utilities = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Mobile Phone' or key == 'Utilities' or key == 'Gym':
            utilities += tally.get(key)
    return utilities

def calc_entertainment_spending():
    tally = tally_categories()
    entertainment = 0
    keys = tally.keys()
    for key in keys:
        if key in {'Movies & DVDs', 'Music', 'Entertainment', 'Sporting Goods'}:
            entertainment += tally.get(key)
    return entertainment

def calc_school_spending():
    tally = tally_categories()
    school_spending = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Books & Supplies' or key == 'Tuition':
            school_spending += tally.get(key)
    return school_spending

def calc_shopping_spending():
    tally = tally_categories()
    shopping = 0
    keys = tally.keys()
    target = ['Shopping', 'Electronics & Software', 'Gift', 'Clothing']
    for key in keys:
        if key in target:
            shopping += tally.get(key)
    return shopping

def calc_misc_spending():
    tally = tally_categories()
    miscellaneous = 0
    keys = tally.keys()
    for key in keys:
        if key == 'Fees & Charges' or key == 'Uncategoried' or key == 'Charity':
            miscellaneous += tally.get(key)
        if key == 'Federal Tax' or key == 'Misc Expenses' or key == 'Bank Fee':
            miscellaneous += tally.get(key)
        if key == 'Business Services':
            miscellaneous += tally.get(key)
    return miscellaneous


# print(tally_categories())
category_to_spent = tally_categories()

to_delete = []
for key, value in category_to_spent.items():
    if value >= 0:
        to_delete.append(key)
    else:
        category_to_spent[key] = category_to_spent[key] * -1

for key in to_delete:
    del category_to_spent[key]

# define function that plots pie chart of spending, input is a dictionary
def plot_pie_chart(category_to_spent):
    sizes = list()
    labels = list()
    for key, value in category_to_spent.items():
        sizes.append(value)
        labels.append(key)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, rotatelabels=45, shadow=True, startangle=90)
    ax1.axis('equal')
    plt.legend(title="Spend Categories")
    plt.savefig("Spending Pie Chart.png")
    plt.show()


# define function that plots line chart of spending over time
#  input is df (transactions data), group by month.
def plot_line_chart(df, year):
    month_to_spending = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
    for index, row in df.iterrows():
        cur_year = row['Date'].split('/')[2]
        cur_month = row['Date'].split('/')[0]
        if cur_year == year:
            if row['Transaction Type'] == 'credit':
                month_to_spending[cur_month] = month_to_spending[cur_month] + row['Amount']
            else:
                month_to_spending[cur_month] = month_to_spending[cur_month] - row['Amount']

    xaxis = []
    yaxis = []
    for key, value in month_to_spending.items():
        xaxis.append(key)
        yaxis.append(value)
        
    # draw line chart with xaxis and yaxis
    plt.plot(xaxis, yaxis)
    plt.xlabel('Month')
    plt.ylabel('Spending')
    plt.title('Spending Over Time')
    plt.savefig("Spending Over Time.png")
    plt.show()


def tally_user_input(tally_dictionary):
    dictionary = {}
    for key, value in tally_dictionary.items():
        dictionary[key] = 0
        

    print(dictionary.keys())
    while True:
        user_input_category = input("Enter 'quit' to stop choosing categories to submit values for or enter category name to set budget: \n")
        if (user_input_category == "quit"):
            break   
        else:
            if (user_input_category) not in dictionary:
                print("Category was not valid")
                continue
            
            user_input_num = int(input("Enter amount to budget: \n"))
            dictionary[user_input_category] = user_input_num

    return dictionary

def budget_left(user_spending, user_budget):

    keys = list(user_spending.keys())

    spending_value = list(user_spending.values())
    for i in np.arange(len(spending_value)):
        spending_value[i] *= -1

    budget_value = list(user_budget.values())
    actual_budget_value = []
    actual_spending_value = []  
    actual_keys = []   
    for key in keys:
        if user_budget[key] > 0:
            actual_budget_value.append(user_budget[key])
            actual_spending_value.append(user_spending[key])
            actual_keys.append(key)


    X_axis = np.arange(len(actual_keys))

    for i in range(len(actual_spending_value)):
        actual_spending_value[i] = actual_spending_value[i] * -1

    plt.bar(X_axis - 0.2, actual_spending_value, 0.4, label = 'Spending')
    plt.bar(X_axis + 0.2, actual_budget_value, 0.4, label = 'Budget')

    plt.xticks(X_axis, actual_keys)
    plt.xlabel("Category")
    plt.ylabel("Amount in Dollars")
    plt.title("Budget and Spending Side-By-Side")
    plt.legend()
    plt.show()


# About the project
# This project is a simple budgeting app that allows you to track your spending and set a budget for each category. 
# The app will then tell you how much you have left to spend in each category. 
# The app will also show you a pie chart of your spending and a line chart of your spending over time.


# This python script will read in your transaction history from a csv file and then display the following:
# 1. The total amount of money in your account
# 2. A pie chart of your spending
# 3. A line chart of your spending over time
# 4. A list of categories and how much you have left to spend in that category

# UNCOMMENT to print out the account balance
#
#
# print(calc_account_balance())

# UNCOMMENT to see pie chart of spending broken down by category
#
#
# plot_pie_chart(category_to_spent)

# UNCOMMENT to have a bar graph that displays spending and budget side by side
# It will prompt for you to choose what categories to input a budget for and how much to budget, type quit to end
#
#
# budget_left(tally_categories(), tally_user_input(tally_categories()))


# UNCOMMENT to see line chart of account balance over time
# Can input different years
#
#
# plot_line_chart(df, '2022')

