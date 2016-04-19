# reliable-sources
This is a command line tool that funnels a list of reliable on-the-scene sources from Twitter into a Google Spreadsheet.

## Set Up and Installation ##
1. Set up [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenv) and cd into it.
2. Run `pip install -r requirements.txt`.
3. Follow instructions in config\_template.py to create your own config.py file.

## Google Drive ##
This repo uses [gspread](https://github.com/burnash/gspread) to connect to Google Drive. Set up a new spreadsheet within your Google Drive, then set up a new project through the [Google Developers Console](https://console.developers.google.com/project). Enable the Google Drive API, and create credentials for a Service Account Key. You will receive a json file with credentials. Follow the template at `credentials_template.json` and rename to `credentials.json`.

You may need to share your Google Spreadsheet with the client_email given to you in `credentials.json`.

We've named our spreadsheet `Reliable Sources`. You can name your spreadsheet whatever you'd like. Simply change the spreadsheet name you call to open in `access.py`.

## Usage ##
`python main.py <location> <optional: keyword>`

Example: `python main.py 'Boston, MA' marathon` or `python main.py Toronto`

## Twython ##
List of interface options available [here](
https://twython.readthedocs.org/en/latest/api.html)
