from __future__ import print_function
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import pandas as pd
import json


json_key = json.load(open("client_secret.json"))
SCOPE = ["https://spreadsheets.google.com/feeds"]
# SCOPE = ["https://www.googleapis.com/auth/drive"]


credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], SCOPE)

# Source dataframe

# Get number of lines and columns


# Function to convert numbers to letters (1->A, 2->B, ... 26->Z, 27->AA, 28->AB...)
def numberToLetters(q):
    q = q - 1
    result = ''
    while q >= 0:
        remain = q % 26
        result = chr(remain+65) + result;
        q = q//26 - 1
    return result

# Test
# print(numberToLetters(27)) # Result : AA)

# Connection to the spreadsheet with the gspread library

# gc = gspread.authorize(user, password)
gc = gspread.authorize(credentials)
def updatesheet(sheet_key,updatedf):
	num_lines, num_columns = updatedf.shape
	ws = gc.open_by_key(sheet_key).sheet1

# Select the range that will be updated ('A1:C3' for example)
	print('A1:'+numberToLetters(num_columns)+str(num_lines))
	cell_list = ws.range('A1:'+numberToLetters(num_columns)+str(num_lines))

	# Modify the values
	for cell in cell_list:
	    val = updatedf.iloc[cell.row-1,cell.col-1]
	    # cell.value = (val.encode('utf-8') if type(val) is str else val)
	    cell.value = val

	# Update in batch
	ws.update_cells(cell_list)

