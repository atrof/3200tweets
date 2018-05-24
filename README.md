# 3200tweets
This script grabs recent 3200+ tweets for a chosen account (-s) using Twitter API and `tweepy` library (Python). 

## Files
* `extractor.py` - main script
* `settings.py` - file for credentials and list of accounts to grab
* `realDonaldTrump_tweets.csv` - output after executing `extractor.py`. A csv-file with tweets and some features from [Donald J. Trump twitter account](https://twitter.com/realDonaldTrump) (grabed on May 24,2018).
* `3200tweets_example.ipynb` - Jupyter Notebook with grabbed data in `pandas.DataFrame()` view

## How to use the script?

1. Install `tweepy`
```
$pip install tweepy
```

2. Create Twitter Application [here](https://apps.twitter.com).

3. Go to the **Keys and Access Tokens** tab.

4. Open `settings.py` and
- Insert your credentials (in single quotes):
```
CONSUMER_KEY = 'Consumer Key (API Key)'`
CONSUMER_SECRET = 'Consumer Secret (API Secret)'`
ACCESS_TOKEN = 'Access Token'`
ACCESS_SECRET = 'Access Token Secret'
```
- Fill the `ACCOUNTS` list with the account (-s) you want to grab (without `@` symbol). For example:
```
ACCOUNTS = ['realDonaldTrump', 'HillaryClinton', 'katyperry', 'jtimberlake']
```

5. Run the script:
```
$python extractor.py
```

6. Wait until you see the notification:
```
Finished!
```

## Grabbed Data
After executing the script you will get csv-file (-s) which contains:
* `account` - account name (nickname)
* `id` - id of the tweet
* `created_at` - date when the tweet was published
* `language` - language of the tweet
* `text` - full text of the tweet
* `likes` - number of likes
* `retweets` - number of retweets
* `hashtags` - hashtag(-s) in the tweet
* `mentions` - account(-s) mentioned in the tweet
* `urls` - url(-s) in the tweet

You can customize which data to grab. Read about [Tweet objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object) and modify `extractor.py` as you wish.

## License
No license. Copy, modify and use without any restrictions.
