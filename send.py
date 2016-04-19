import gspread
import sys

from access import get_google_sheet
from datetime import date, datetime

def send_to_google_drive(reliable_tweets):
    #open google sheet
    sheet = get_google_sheet()

    #set the title of the worksheet user's location input as the title of the worksheet
    worksheet_name = sys.argv[1]

    #find and format the date to add to worksheet title
    today = date.today()
    created_on = datetime.now().strftime('%m-%d, %Y: %H:%M:%S')

    #create a new worksheet with a title of the location and date
    new_worksheet = sheet.add_worksheet(title=worksheet_name+": "+created_on, rows="100", cols="20")

    #set headers
    new_worksheet.update_cell(1, 1, 'User')
    new_worksheet.update_cell(1, 2, 'Tweet')
    new_worksheet.update_cell(1, 3, 'Timestamp')

    #start filling data at the second row of the worksheet, as the first is populated with headers
    i = 2

    #iterate through each reliable tweet to fill the rows of the worksheet
    for tweet in reliable_tweets:
        username = tweet[0]['user']['screen_name']
        tweet_content = tweet[0]['text']
        timestamp = tweet[0]['created_at']

        new_worksheet.update_cell(i, 1, username)
        new_worksheet.update_cell(i, 2, tweet_content)
        new_worksheet.update_cell(i, 3, timestamp)
        i+=1
    
