from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def send_to_google_drive():
    #set oauth
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    #create spreadsheet within google drive
    spreadsheet = drive.CreateFile({'title': 'test', 'mimeType': 'application/vnd.google-apps.spreadsheet'})

    #update spreadsheet
    spreadsheet.Upload()
