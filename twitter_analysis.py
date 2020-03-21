import GetOldTweets3 as got

text_tweets = []
def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Corona virus') \
        .setSince("2019-12-29") \
        .setUntil("2020-03-20") \
        .setMaxTweets(10)
    # List of objects gets stored in tweets variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    #for tweet in tweets:
        #text_tweets.append([tweet.text])

    #print(text_tweets)
                          #OR
    for tweet in tweets:
         text_tweets = [[tweet.text] for tweet in tweets]

    print(text_tweets)

get_tweets()
