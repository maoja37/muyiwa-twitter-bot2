import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("IZRBmm1NssWTUytF9bI41VRVj")
API_SECRET = os.getenv("aOIUNmbAT6ArKYVbH237W6mtWY7r7qTubLY901YHicKlcd9nAp")
ACCESS_TOKEN = os.getenv("1278003016977854464-1ZcnVdbh5SVmLcQklj0mfFxdWTMyGY")
ACCESS_SECRET = os.getenv("duEVCFdEyHzDitZ6iwSNNohlZu3m4zVZIHzhzz921gy88")

auth = tweepy.OAuthHandler("IZRBmm1NssWTUytF9bI41VRVj", "aOIUNmbAT6ArKYVbH237W6mtWY7r7qTubLY901YHicKlcd9nAp")
auth.set_access_token("1278003016977854464-1ZcnVdbh5SVmLcQklj0mfFxdWTMyGY", "duEVCFdEyHzDitZ6iwSNNohlZu3m4zVZIHzhzz921gy88")

api = tweepy.API(auth)

tweet_list = api.favorites(screen_name='MuyiwaOyinloye', count=5)

#print the id for each of the tweets
# for tweet in tweet_list:  
#     print(tweet.id)



# api.retweet(tweet_id)

for tweet in api.favorites(screen_name='MuyiwaOyinloye'):
    try:
        api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(e)


