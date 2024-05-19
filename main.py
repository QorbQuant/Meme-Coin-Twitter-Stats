import tweepy
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import config


print(config.BEARER_TOKEN)
# Authenticate with the Twitter API using credentials from config.py
client = tweepy.Client(bearer_token=config.BEARER_TOKEN)


# Function to get tweets from a user
def get_tweets(username, max_results=100):
    user = client.get_user(username=username)
    user_id = user.data.id
    
    tweets = client.get_users_tweets(
        id=user_id,
        tweet_fields=["created_at", "public_metrics"],
        max_results=max_results
    )
    return tweets.data

# Fetch tweets from the user
username = "degenerate_defi"
tweets = get_tweets(username)

# Extract data
data = []
for tweet in tweets:
    created_at = tweet.created_at.strftime("%Y-%m-%d")
    likes = tweet.public_metrics["like_count"]
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
