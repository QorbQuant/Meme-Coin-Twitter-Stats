import tweepy
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Import Twitter API credentials from config.py
import config

# Authenticate with the Twitter API using credentials from config.py
auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to get tweets from a user
def get_tweets(username, count=200):
    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items(count):
        tweets.append(tweet)
    return tweets

# Fetch tweets from the user
username = "TwitterUsername"
tweets = get_tweets(username)

# Extract data
data = []
for tweet in tweets:
    created_at = tweet.created_at.strftime("%Y-%m-%d")
    likes = tweet.favorite_count
    data.append([created_at, likes])

# Save data to a DataFrame
df = pd.DataFrame(data, columns=["Date", "Likes"])

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Group by Date to get the total likes per day
df_grouped = df.groupby("Date").sum().reset_index()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df_grouped["Date"], df_grouped["Likes"], marker='o')
plt.title("Likes Per Tweet Over Time")
plt.xlabel("Date")
plt.ylabel("Total Likes")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
