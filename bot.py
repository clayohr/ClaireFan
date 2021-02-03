import tweepy 
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
from dotenv import load_dotenv
load_dotenv()
import os
import random




consumer_key = os.getenv("CONSUMER_KEY")

consumer_secret = os.getenv("CONSUMER_SECRET")

key = os.getenv("KEY")

secret = os.getenv("SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

words = [
    'cute', 'smile', 'pretty', 'I love you', 'smiling', 'magnificent',
     'wonderful', 'soaring', 'beautiful', 'love',
    'cutie', 'perfect', 'beloved', 'dazzle', 'sparkling', 'sparkle', 'loving', 'sweet',
    'amazing', 'Im smiling', 'dear', 'sweetheart', 'baby', 'savant', 'genius', 'you are', 'swag', 'ultimate', 'OMG',
    'LOL', 'virtuoso', 'breathtaking', 'inspiring'
]


class StdOutListener(StreamListener):
    def on_data(self, data):
        clean_data = json.loads(data)
        tweetId = clean_data["id"]
        user_id = clean_data['user']['id']
        tweet = random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + "!!!!"
        if user_id == 2941719227:
            print("oh yeah game time")  # optional
            respondToTweet(tweet, tweetId)
            
            



def followStream():
    listener = StdOutListener()
    stream = Stream(auth, listener)
    stream.filter(follow=["2941719227"], is_async=True)


def respondToTweet(tweet, tweetId):
    api.update_status(tweet, in_reply_to_status_id=tweetId, auto_populate_reply_metadata=True)



if __name__ == "__main__":
    followStream()



