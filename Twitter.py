import string
import tweepy
import csv
import re
import preprocessor as p
consumer_key = 'S9s9Ll9Wf6YZk4792iChDKsIp'
consumer_secret = 'uwKTjmdOY0CSmGpGRIZK2z6jtPHMekSa0qEy7EnhqPzAYRtHdp'
access_key= '353755144-bdFrZOGMTZGBC4maUHqLC6ND92DUdqKy0chkaGC7'
access_secret = 'LUH44JcOYYHj9Df7W09CD8a93VqPK3KqLz7OccZVaBF1Z'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
csvFile = open('file-name', 'a')
csvWriter = csv.writer(csvFile)
search_words = "Messi"      #enter your words
new_search = search_words + " -filter:retweets"
for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=10,
                           lang="en",
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])