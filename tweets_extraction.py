import tweepy
import csv
import pandas as pd
####input your credentials here
  consumer_key ="1272794785690947584-ebJdyesr11s75hESVvs5kbbbfDiVsy"
  consumer_secret = "L9nBWeqgfFFmdPW45ATvDZ7W3tfEpblodfH0ISLMqnv20"
  access_token = "I6JV64tnXF04utLo73D8uzpc7"
  access_token_secret = "lP4uVWUGXEUZX3M9VAP9wbyjsrIbt5UshKeJGIbMqblwohqsJr"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
# Open/Create a file to append data
csvFile = open('2.csv', 'a')
#Use csv Writer
      csvWriter = csv.writer(csvFile)
      for tweet in tweepy.Cursor(api.search,q="#fuckyou",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
