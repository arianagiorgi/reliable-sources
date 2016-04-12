import json
from twython import Twython

from config import (consumer_key, consumer_secret, access_token, access_token_secret)

def filter_sources(tweet):
	### TK

	pass

def find_tweets(twitter, place_id):
	### Return tweets from a certain place id

	#`count` param defaults to 15, maximum of 100. using 3 for now to test
	results = twitter.search(q = 'place:'+place_id, count = '3')

	#turn results in json string
	tweets = json.loads( json.dumps(results) )

	print "Tweets:"
	for i in range(len(tweets['statuses'])):
		tweet_id = tweets['statuses'][i]['id_str']

		#retrieve tweet based on tweet_id
		t = twitter.lookup_status(id = tweet_id)
		tweet = json.loads( json.dumps(t) )

		#sample parse for tweet output
		print tweet[0]['user']['screen_name']+': '+tweet[0]['text']

		#this is where we're going to filter these tweets then return
		#filter_sources(tweet)

		#pydrive?



def find_place(location):
	### Determine place id based on querying location

	#configure twython connection
	twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

	results = twitter.search_geo(query = location, max_results = '3')
	
	#turn results into json string, then turn json string into parsable dictionary
	locations = json.loads( json.dumps(results) )

	#results return different location possibilities based on the location you enter
	#we need the user to tell us which location is the right one to use
	print "Results based on your provided location:"
	for i in range(len(locations['result']['places'])):
		print str(i+1)+'. ', locations['result']['places'][i]['full_name']
		### TODO: option for "other"

	place_number = input('Please enter the location you want to use: ')
	place_number = place_number - 1 #adjust for array counting

	place_id = locations['result']['places'][place_number]['id']

	find_tweets(twitter, place_id)


