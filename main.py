import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from func import *

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Test").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell

name = str(input("Enter your name: "))
row = int(input("Enter number your row(example: 1): "))
column = int(input("Enter number your column(example: 1): "))
sheet.update_cell(row, column, name)
  # Update one cell
