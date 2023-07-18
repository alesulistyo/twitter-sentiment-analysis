import tweepy
import csv
import string
import sys
from tweepy import OAuthHandler

api_key = "CaeI1YNTNUiTE4Dct2oR2lyss"
api_secret_key = "GjAhkid8NDOepjhnHFXsPcCadXJnwNAq9nFGOBCtWe2zyrICzs"
access_token = "1260432503548129280-Lu7xoPAxrnJQacp4oMKjNe51SIljYN"
access_token_secret = "Q8abqMRAEpcjnCYq0QBOULQp29OXfCixrxuIlLtjwQDJt"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

csvFile = open('hasil_crawling.csv', 'a', encoding='utf-8')
csvWriter = csv.writer(csvFile)

csvWriter.writerow(["tanggal", "pengguna", "tweets"])
for tweet in tweepy.Cursor(api.search, q="kuliah online -filter:retweets", lang="id", tweet_mode='extended').items(int(sys.argv[1])):
    csvWriter.writerow(
        [tweet.created_at, tweet.user.screen_name, tweet.full_text])
