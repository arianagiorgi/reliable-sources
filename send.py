import sys

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import date

def send_to_google_drive(reliable_tweets):
    #set oauth
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    #set the title of the spreadsheet user's location input as the title of the spreadsheet
    spreadsheet_name = sys.argv[1]

    #find and format the date to add to spreadsheet title
    today = date.today()
    created_on = today.strftime('%b %d, %Y')

    #create spreadsheet within google drive
    spreadsheet = drive.CreateFile({'title': spreadsheet_name+": "+created_on, 'mimeType': 'text/csv'})

    #update spreadsheet
    content = 'User, Tweet, Timestamp\n'

    for tweet in reliable_tweets:
        username = tweet[0]['user']['screen_name']
        tweet_content = tweet[0]['text']
        timestamp = tweet[0]['created_at']
        content += username+','+tweet_content+','+timestamp+'\n'

    spreadsheet.SetContentString(content)
    spreadsheet.Upload(param={'convert': True})
