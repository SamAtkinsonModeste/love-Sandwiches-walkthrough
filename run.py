#Below imports the entire gspread library,
#So we can access any functions,class or methods
import gspread
#Below imports the Credentials class,
#which is part of the service_account  function from the Google auth library.
#As we only need this class for our project, there  is no need to import the entire library here.
from google.oauth2.service_account import Credentials


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
    print('Please enter sales data from the last market.')
    print('Data should be six numbers,separated by commas.')
    print('Example: 10,20,30,40,50,60\n')

    data_str = input('Enter your data here:  ')
  
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string value into integers.
    Raises ValueError if strings cannot convert into int,
    or if there aren't exactly 6 values.
    """
    try: 
          if len(values) != 6:
               raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}" 
               )
    except ValueError as e:
          print(f'Invalid data: {e}, please try again.\n')
          
    



get_sales_data()





