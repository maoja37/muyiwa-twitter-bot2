import tweepy

# tweepy authentication function
def tweepy_auth(API_KEY , API_SECRET , ACCESS_TOKEN, ACCESS_SECRET):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth) 
    return api

# tweepy retweet likes function
def retweet_timeline(api, username):
    for tweet in api.user_timeline(username , include_rts = False):
        try:
            api.unretweet(tweet.id)
            api.create_favorite(tweet.id)
        except tweepy.TweepError as e:
            print(e)

    return print("Done")