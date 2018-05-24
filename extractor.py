import tweepy
import csv
from settings import *

def extract(screen_name):
    
    #authorizing twitter and initializeing tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    #initializing empty list for holding extracted tweets
    tweets = []
    
    #requesting for recent 200 tweets (allowed maximum)
    new_tweets = api.user_timeline(screen_name = screen_name, count=200, tweet_mode = 'extended')
    
    #saving the most recent tweets to the earlier initialized list
    tweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest_id = tweets[-1].id - 1
    
    #getting tweets while it`s possible
    while len(new_tweets) > 0:
                
        new_tweets = api.user_timeline(screen_name = screen_name, 
                                       count = 200, 
                                       tweet_mode = 'extended', 
                                       max_id = oldest_id)
        tweets.extend(new_tweets)
        oldest_id = tweets[-1].id - 1
        
    #getting the neccessary fields from recieved json to save in csv
    output = [[tweet.user.screen_name, 
               tweet.id_str,
               tweet.created_at,
               tweet.lang, 
               #removing special symbols
               tweet.full_text.replace('\n', ' ').replace('\r', ''), 
               tweet.favorite_count, 
               tweet.retweet_count, 
               #hashtags
               ', '.join(['#{}'.format(hashtag['text']) for hashtag in tweet.entities['hashtags']]),
               #mentioned account (-s)
               ', '.join(['@{}'.format(mention['screen_name']) for mention in tweet.entities['user_mentions']]), 
               #urls
               ', '.join(['{}'.format(url['url']) for url in tweet.entities['urls']]), 
              ] for tweet in reversed(tweets)]
    
    print('>>>{} tweets were extracted from @{} account'.format(len(output), account))
    
    #writing tweets to the csv-file
    with open('%s_tweets.csv' % screen_name, 'w') as f:
        
        writer = csv.writer(f)
        writer.writerow(['account', 
                         'id', 
                         'created_at', 
                         'language', 
                         'text', 
                         'likes', 
                         'retweets',
                         'hashtags',
                         'mentions',
                         'urls'])
        writer.writerows(output)
        
    pass

for account in ACCOUNTS:
    extract(account)
