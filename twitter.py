#!/usr/bin/python3
#  -*- coding: utf-8 -*-
# tweepy-bots/bots/autoreply.py

# Date: Fri 21 May 2021 10:05:31 CEST
# Author: Marina Mougammadaly
# Last updated by: Marina Mougammadaly
# Last updated date: Fri 21 May 2021 10:05:31 CEST
# Description: Zoltar Project - ECAM - EENG 1

import os #(This is Optional and only used if you set your API keys and Token in your OS environments)
from datetime import datetime as dt
from datetime import timedelta
import tweepy
from Bot import random_bot
import json
from twitter_keys import keys # import the dict keys from my file twitter_keys

	#........Setup access to API........
auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])

	#........Create an object........
api = tweepy.API(auth)#, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def auth():
	try:
		api.verify_credentials()
		print("Authentication OK")
	except:
		print("Error during authentification")

def tweets():	
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		print(tweet.text)
		print(tweet.id)
		#print(tweet.screen.name)
def write_tweet():
	message = "Welcome to the Zoltar Machine. Ask your question and we will predict your future."
		
	try:	
		api.update_status(status = message)
	except:
		print("Issue")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

FILE = 'data.json'


def tweet_15min():
	if last_tweeted< datetime.now()- timedelta(hours=0.25):
		api.status(random_bot)
		logger.info(f"Tweeted {text}at{datetime.now().strftime('%m/%d/%Y at %H:%M:%S')
		return datetime.now()
	else:
		return last_tweeted

# 


#auth()		
tweets()
check_mentions() 	




