# reliable-sources
Project to return a list of reliable on-the-scene sources from Twitter. Currently, just running from the command line. 

## Set up and Installation ##
1. Set up [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenv) and cd into it
2. Run `pip install -r requirements.txt`
3. Follow instructions in config\_template.py in order to create your own config.py file
4. Follow instructions in client\_secrets\_template.json in order to set up your own client\_secrets.json file
5. 

## Usage ##
`python main.py <location> <optional: keyword>`

Example: `python main.py 'Boston, MA' marathon`
or `python main.py Toronto`

## Twython ##
List of interface options available [here](
https://twython.readthedocs.org/en/latest/api.html)