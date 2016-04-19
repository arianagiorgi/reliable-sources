import json
import gspread

from oauth2client.client import SignedJwtAssertionCredentials

#access google spreadsheet
def get_google_sheet():
    json_key = json.load(open('credentials.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key["client_email"], json_key['private_key'], scope)
    authorization = gspread.authorize(credentials)
    spreadsheet = authorization.open("Reliable Sources")
    return spreadsheet
