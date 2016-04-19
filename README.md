# reliable-sources
Project to return a list of reliable on-the-scene sources from Twitter.

## Set up and Installation ##
Set up virtualenv

Run `pip install -r requirements.txt`

## Usage ##
`python main.py <Location>`

Example: `python main.py Toronto`

## Twython ##
List of interface options available [here](
https://twython.readthedocs.org/en/latest/api.html)

## Google Drive ##

We use gspread to connect to Google Drive. Set up a new spreadsheet within your Google Drive, then follow instructions to obtain OAuth Credentials: http://gspread.readthedocs.org/en/latest/oauth2.html

You'll want to create a service account, and you'll receive a json file with credentials. Follow the template at `credentials_template.json` and rename to `credentials.json`.

We've named our spreadsheet `Reliable Sources`. You can name your spreadsheet whatever you'd like. Simply change the spreadsheet name you call to open in `access.py`.
