import tweepy
import config

# Authenticate with the Twitter API using credentials from config.py
client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

# Function to get user information
def get_user_info(username):
    try:
        user = client.get_user(username=username)
        return user.data
    except tweepy.TweepyException as e:
        print(f"Error: {e}")

# Fetch user info
username = "TwitterUsername"
user_info = get_user_info(username)
if user_info:
    print(f"User ID: {user_info.id}, Username: {user_info.username}, Name: {user_info.name}")
