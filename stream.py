
import tweepy
from random import randint
from dotenv import load_dotenv
from datetime import date
import os
import time
from win10toast import ToastNotifier
import webbrowser
from tweepy import Stream


class IDPrinter(tweepy.Stream):

    def on_status(self, tweet):
        if tweet.text[:2]=="RT" or tweet.text[:1]=="@" :
            return
        
        toast = ToastNotifier()
        toast.show_toast(title = 'user: {} tweeted:'.format(tweet.user.name),msg =tweet.text,duration = 10,icon_path = os.getenv('icon'),callback_on_click=lambda:gototweet(tweet.id))

def gototweet(id):
    webbrowser.open('https://twitter.com/twitter/statuses/'+str(id))



def run():
    load_dotenv()
    CONSUMER_KEY=os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET=os.getenv('CONSUMER_SECRET')
    ACCESS_KEY=os.getenv('ACCESS_KEY')
    ACCESS_SECRET= os.getenv('ACCESS_SECRET')
    keywords=os.getenv('keyword')
    printer = IDPrinter(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
    printer.filter(track=[keywords])


if __name__ == '__main__':
    run()