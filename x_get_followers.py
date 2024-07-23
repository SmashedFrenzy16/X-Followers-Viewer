import tweepy

bot = tweepy.Client(consumer_key="ENTER CONSUMER KEY HERE",
                    consumer_secret="ENTER CONSUMER SECRET HERE",
                    access_token="ENTER ACCESS TOKEN HERE",
                    access_token_secret="ENTER ACCESS TOKEN SECRET HERE")

user_id = "ENTER USER ID HERE"

followers = bot.get_users_followers(id=user_id)

print(followers)

