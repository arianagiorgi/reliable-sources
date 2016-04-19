import gspread
import sys
from datetime import date, datetime

from access import get_google_sheet

def fetch_data(tweet):
    username = tweet[0]['user']['screen_name']
    tweet_content = tweet[0]['text']
    timestamp = tweet[0]['created_at']

    #number of followers user has
    followers = tweet[0]['user']['followers_count']

    #check if there's an image included
    text = tweet[0]['text'].lower()

    if 't.co' in text:
		image = 'Yes'
    else:
		image = 'No'

	#favorites and retweets
    favorites = tweet[0]['favorite_count']
    retweets = tweet[0]['retweet_count']

    return username, tweet_content, timestamp, followers, image, favorites, retweets

def send_to_google_drive(reliable_tweets):
    #open google sheet
    sheet = get_google_sheet()

    #set the title of the worksheet user's location input as the title of the worksheet
    worksheet_name = sys.argv[1]

    #find and format the date to add to worksheet title
    today = date.today()
    created_on = datetime.now().strftime('%m-%d, %Y: %H:%M:%S')

    #create a new worksheet with a title of the location and date
    new_worksheet = sheet.add_worksheet(title=worksheet_name+": "+created_on, rows="101", cols="20")

    #set headers
    new_worksheet.update_cell(1, 1, 'User')
    new_worksheet.update_cell(1, 2, 'Tweet')
    new_worksheet.update_cell(1, 3, 'Timestamp')
    new_worksheet.update_cell(1, 4, 'Followers')
    new_worksheet.update_cell(1, 5, 'Image?')
    new_worksheet.update_cell(1, 6, 'Favorites')
    new_worksheet.update_cell(1, 7, 'Retweets')

    #start filling data at the second row of the worksheet, as the first is populated with headers
    i = 2

    #iterate through each reliable tweet to fill the rows of the worksheet
    for tweet in reliable_tweets:

    	username, tweet_content, timestamp, followers, image, favorites, retweets = fetch_data(tweet)

        new_worksheet.update_cell(i, 1, username)
        new_worksheet.update_cell(i, 2, tweet_content)
        new_worksheet.update_cell(i, 3, timestamp)
        new_worksheet.update_cell(i, 4, followers)
        new_worksheet.update_cell(i, 5, image)
        new_worksheet.update_cell(i, 6, favorites)
        new_worksheet.update_cell(i, 7, retweets)

        i+=1
