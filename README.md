# Twitter PC Notifier:
This is a twitter notifiter for windows 10 that brings clickable tweets of your choice to your notification center, Made using tweepy and win10toast libraries   

## requirements:
-tweepy 4.2.0  
-a very specific version of win10toast (a fork of the original implemented the ability to click the notification but was failing on install due to requirments conflicts so i searched for forks that worked and got one)
you can install it using:
```
pip3 install git+https://github.com/WeebMogul/Windows-10-Toast-Notifications
```

## methods of running:
There are two scripts:  
**search.py:** this script fetches tweets first through your desired keyword and filters the retweets and replys and goes through them before fetching new ones with a date closer to the last tweet fetched, this method works best with keyword that are not largely popular and might miss a tweet or two but it's always gonna bring up the latest tweet. 

**stream.py:** this one uses the stream function in the tweepy library to always constantly bring up the latest tweets but queuing tweets might be a minute late or so if it's a largly popular keyword.


## to be added:
1-Mobile notifications  
2-Profiling    
3-Sentiment Analysis for tweets    
