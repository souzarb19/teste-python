import oauth2
import tweepy


cliente = tweepy.Client(consumer_key='',
                        consumer_secret='',
                        access_token='',
                        access_token_secret='')

tweet = input('#Tweet: ')
cliente.create_tweet(text=tweet)
