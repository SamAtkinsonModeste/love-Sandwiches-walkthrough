#Below imports the entire gspread library,
#So we can access any functions,class or methods
import gspread
#Below imports the Credentials class,
#which is part of the service_account  function from the Google auth library.
#As we only need this class for our project, there  is no need to import the entire library here.
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches-2')

sales = SHEET.worksheet('sales')
data = sales.get_all_values()

print(data)
