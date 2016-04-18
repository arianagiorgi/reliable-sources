import sys

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import date

def send_to_google_drive():
    #set oauth
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    #set the title of the spreadsheet user's location input as the title of the spreadsheet
    spreadsheet_name = sys.argv[1]

    #find and format the date to add to spreadsheet title
    today = date.today()
    created_on = today.strftime('%b %d, %Y')

    #create spreadsheet within google drive
    spreadsheet = drive.CreateFile({'title': spreadsheet_name + ": " + created_on, 'mimeType': 'application/vnd.google-apps.spreadsheet'})

    #update spreadsheet
    spreadsheet.Upload()
