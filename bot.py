import tweepy
import config
import random

print("PLAYER 1 HAS JOINED")
#Schedule is mon-Fri at 6:30 am ETC

auth = tweepy.OAuth1UserHandler(config.consumer_key, config.consumer_secret, config.access_token, config.access_token_secret
)

api_m = tweepy.API(auth) 

bot_id = 1123691907069161472

soundtrack_list = ["https://www.youtube.com/watch?v=T_daENWiDAA , https://www.youtube.com/watch?v=GYE9H4SMq5E , https://www.youtube.com/watch?v=pZ6oeHV28b0 , https://www.youtube.com/watch?v=goYgHnsQdtY , https://www.youtube.com/watch?v=fazMSCZg-mw , https://www.youtube.com/watch?v=T8e5YMKVQXU , https://www.youtube.com/watch?v=zbWpjizpJfI , https://www.youtube.com/watch?v=m1a_GqJf02M , https://www.youtube.com/watch?v=OlStmta0Vh4 , https://www.youtube.com/watch?v=YY2ng9SjCTo , https://www.youtube.com/watch?v=GfiJowcJiVw , https://www.youtube.com/watch?v=3_g2un5M350 , https://www.youtube.com/watch?v=T0pYq_Saf7g , https://www.youtube.com/watch?v=QLCpqdqeoII"];
soundtrack_list_length = len(soundtrack_list)

#change this ^ up here to make it customized and switch ur keys out. 

def player1(twt):
    the_id = twt.id
    name = twt.author.screen_name
    i = random.randint(0, soundtrack_list_length)
    message = f"@{name} Here's your song! 🎮 {soundtrack_list[i]}"

    print("Tweet Found!")
        #twt.author.screen_name, etc, are taken from Twitter docs LINK HERE
    print(f"TWEET: {name} - {twt.text}")
    if ((twt.author.id != bot_id) and not (hasattr(twt, "quoted_status")) and not (hasattr(twt, "retweeted_status"))):
        try:
            the_tweet = twt.extended_tweet["full_text"]
        except AttributeError:
            the_tweet = twt.text
        #tweet has "Weeknd" and "song" in it
        if ("Weeknd" in the_tweet) and ("song" in the_tweet):
            try:
                print("Attempting Comment")
                api_m.update_status(status = message, in_reply_to_status_id = the_id)
                print("TWEET SUCCESSFUL")
            except Exception as err:
                print(err)
        else:
            print("oops")
    else:
        print("oops twice")
class MyStreamListener(tweepy.Stream):
#on_status is what happens when a status ("tweet") comes into the stream
    def on_status(self, twts):
        player1(twts)               

         
#create instance
stream_m = MyStreamListener(config.consumer_key, config.consumer_secret, config.access_token, config.access_token_secret)
#use "follow" for RT a specific account, "track" for tweets that contain the word
stream_m.filter(track =["Weeknd & Future"])
