from twython import Twython
from config import (consumer_key, consumer_secret, access_token, access_token_secret)
from send import send_to_google_drive

def filter_tweets(tweet, keyword):
	### method to filter out tweets that might be spam
	### edit omit.txt to update a list of keywords you want to exclude

	#filter based on keywords in text
	text = tweet[0]['text'].lower()

	with open('omit.txt', 'r') as f:
		#open file with keywords and test them against the tweet
		for line in f:
			omitted_word = line.lower().rstrip()

			if omitted_word in text:
				#if a keyword appears in the tweet, it's not a reliable tweet
				return False

	return True


def find_tweets(twitter, place_id, keyword):
	### return tweets from a certain place_id

	#`count` param defaults to 15 with a maximum of 100
	if keyword == '':
		tweets = twitter.search(q = 'place:'+place_id, count = '15')
	else:
		tweets = twitter.search(q = 'place:'+place_id+' '+keyword, count = '15')

	reliable_tweets = []

	for i in range(len(tweets['statuses'])):
		tweet_id = tweets['statuses'][i]['id_str']

		#retrieve tweet based on tweet_id
		tweet = twitter.lookup_status(id = tweet_id)

		#send tweets through the filter
		reliable = filter_tweets(tweet, keyword)

		if reliable == True:
			#print tweet[0]['user']['screen_name']+': '+tweet[0]['text']
			reliable_tweets.append(tweet)

	send_to_google_drive(reliable_tweets)


def find_place(location, keyword=''):
	### determine place id based on querying location

	#configure twython connection
	twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

	locations = twitter.search_geo(query = location, max_results = '5')

	#return different location possibilities based on the location entered
	print "Results based on your provided location:"
	for i in range(len(locations['result']['places'])):
		print str(i+1)+'. ', locations['result']['places'][i]['full_name']

	place_number = input('Please enter the location you want to use: ')

	#adjust for array counting
	place_number = place_number - 1

	place_id = locations['result']['places'][place_number]['id']

	find_tweets(twitter, place_id, keyword)
