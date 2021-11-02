import tweepy
import time
from dotenv import load_dotenv
import os
import time
from win10toast import ToastNotifier
import webbrowser

def apiAuthenticaion():
    load_dotenv()
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    ACCESS_SECRET = os.getenv('ACCESS_SECRET')
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def fetchtweets(api,keywords,lastid):
    try:
        tweets = tweepy.Cursor(api.search_tweets,q=keywords,since_id=lastid).items(50)
        x=[{"text":tweet.text,'user':tweet.user.name,"id":tweet.id} for tweet in tweets]
        print("Fetched " + str(tweets.num_tweets)+ " tweets for the term " + str(keywords))
        return x

    except:
        print("Unfortunately, something went wrong..")
        return None


def getlastid(api,keywords):
    tweets=tweepy.Cursor(api.search_tweets,q=keywords,result_type='recent').items(5)
    x=[{"text":tweet.text,'user':tweet.user.name,"id":tweet.id} for tweet in tweets]
    y=x[-1:]
    return y[0]['id']
        
def gototweet(id):
    webbrowser.open('https://twitter.com/twitter/statuses/'+str(id))


def run():
    api=apiAuthenticaion()
    lastid=getlastid(api,os.getenv('keyword'))
    id=[]
    id.append(lastid)
    toast = ToastNotifier()
    while True:
        lastid=id[-1]
        tweets=fetchtweets(api,os.getenv('keyword'),lastid)
        print(tweets)
        for tweet in tweets:
            if tweet['text'][:2]=="RT" or tweet['text'][:1]=="@" :
                continue
            if tweet['id'] not in id:
                toast.show_toast(title = 'user: {} tweeted:'.format(tweet['user']),msg =tweet['text'],duration = 10, icon_path = os.getenv('icon'),callback_on_click=lambda:gototweet(tweet['id']))
                id.append(tweet['id'])
                time.sleep(10)
            else:
                continue
        time.sleep(10)

if __name__ == '__main__':
    run()