# Reliable Sources
This is a command line tool that funnels a list of reliable on-the-scene sources from Twitter into a Google Spreadsheet.

This open-source project was created by [Sara Simon](https://github.com/smbsimon) and [Ariana Giorgi] (https://github.com/arianagiorgi). Thanks to OpenNews for their support.

## Set Up and Installation ##
1. Set up [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenv) and cd into it.
2. Run `pip install -r requirements.txt`.
3. Follow instructions in config\_template.py to create your own config.py file.
4. Follow instructions to connect to Google Drive [below](https://github.com/arianagiorgi/reliable-sources#google-drive).
5. You're ready to go! See usage [examples](https://github.com/arianagiorgi/reliable-sources#examples).

## Google Drive ##
This repo uses [gspread](https://github.com/burnash/gspread) to connect to Google Drive. Set up a new spreadsheet within your Google Drive, then set up a new project through the [Google Developers Console](https://console.developers.google.com/project). Enable the Google Drive API, and create credentials for a Service Account Key. You will receive a json file with credentials. Follow the template at `credentials_template.json` and rename to `credentials.json`.

You may need to share your Google Spreadsheet with the client_email given to you in `credentials.json`.

We've named our spreadsheet `Reliable Sources`. You can name your spreadsheet whatever you'd like. Simply change the spreadsheet name you call to open in `access.py`.

## Usage ##
`python main.py <location> <optional: keyword>`

### Examples ###
To search for any tweet out of Toronto: `python main.py 'Toronto'`

To search for tweets relating to the Boston marathon:
 `python main.py 'Boston, MA' 'marathon'` or for a certain hashtag: `python main.py 'Boston, MA' '#MarathonMonday'`

To search for tweets in New York mentioning Bernie Sanders:
`python main.py 'New York, NY' '@BernieSanders'`

To search multiple hashtags, just extend the keyword string:
`python main.py 'New York, NY' '#feelthebern #latinosforbernie'`

Some locations may be too specific for Twitter. On April 19th there was an explosion heard in Kabul, Afghanistan. To find relevant tweets, you can use:
`python main.py 'Afghanistan' 'kabul'` or to be more specific, `python main.py 'Afghanistan' 'kabul blast'`

To search for pictures or videos of bikes in Austin:
`python main.py 'Austin' 'bike filter:media'`

The Twitter API provides many other query operator examples [here](https://dev.twitter.com/rest/public/search).

## Twython ##
A list of interface options is available [here](https://twython.readthedocs.org/en/latest/api.html).
