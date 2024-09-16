#Below imports the entire gspread library,
#So we can access any functions,class or methods
import gspread
#Below imports the Credentials class,
#which is part of the service_account  function from the Google auth library.
#As we only need this class for our project, there  is no need to import the entire library here.
from google.oauth2.service_account import Credentials
#Installing PPRINT
from pprint import pprint


#Every Google account has an IAM configuration.
#IAM stands for Identity and Acess Management. This configuration specifies what the user has access to.
#The scope lists the APIs that the program should access in order to run
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

#We call the from_service_account_file method of the Credentials class
#and pas  it our creds.json file name
CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches-2')

def get_sales_data():
    '''
    Get sales figures input from the user
    '''
    while True:
        print('Please enter sales data from the last market.')
        print('Data should be six numbers,separated by commas.')
        print('Example: 10,20,30,40,50,60\n')

        data_str = input('Enter your data here:  ')
    
        sales_data = data_str.split(",")
    
        if validate_data(sales_data):
             print("Data is valid")
             break
        
    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string value into integers.
    Raises ValueError if strings cannot convert into int,
    or if there aren't exactly 6 values.
    """
    try: 
          #List comprehension that turns all strings to integers
          [int(value) for value in values]
          if len(values) != 6:
               raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}" 
               )
    except ValueError as e:
          print(f'Invalid data: {e}, please try again.\n')
          return False

    return True
          
    

def update_sales_worksheet(data):
     """
     Update sales worksheet, and add new row with the list data provided.
     """
     print("Updating sales worksheet...\n")
     #To access our worksheets we create a variable sales_worksheet an assign it our variable SHEET
     #The SHEET variable uses the gspread library
     #We use the gspread worksheet()  method to access our sales worksheet.
     #The value we put in worksheet() relates to the name of our worksheet.
     sales_worksheet = SHEET.worksheet("sales")
     #We now use a gspread Method called append_row() and pass it our data to be inserted
     #The append_row method adds a new row to the  end of our data in the worksheet selected.
     sales_worksheet.append_row(data)
     print("Sales works updated successfully.\n")

def calculate_surplus_data(sales_row):
     """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
     """
     print("Caluculating surplus data...\n")
     #In order to calculate our surplus, we also  need our stock data for before the market from the stock worksheet.
     stock = SHEET.worksheet("stock").get_all_values()
     #We use pprint() method here instead of the standard  print statement, so our data is easier to read
     #pprint(stock)
     #Variable for the last row in our stock worksheet
     #By using Slice
     stock_row = stock[-1]
     print(stock_row)






#It's common practice to wrap the main function calls of a program within a function called main.
def  main():
    """
    Run all program functions
    """
    data = get_sales_data()
    #when we print our data below it returns a list of strings.
    #print(data)
    #['1', '2', '3', '4', '5', '6']
    #In order for our spreadsheet to accept it, we need to convert these  values into integers.
    #We will convert the above string with a List Comprehension
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)

print("Welcome to Love Sandwiches Data Automation\n")
main()







