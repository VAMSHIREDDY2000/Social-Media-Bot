import tweepy
import time

# Set up your API keys here (replace with your own keys from Twitter Developer)
API_KEY = 'your-api-key'
API_SECRET_KEY = 'your-api-secret-key'
ACCESS_TOKEN = 'your-access-token'
ACCESS_TOKEN_SECRET = 'your-access-token-secret'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Function to post a tweet
def post_tweet(text):
    try:
        api.update_status(text)
        print("Tweet posted successfully.")
    except tweepy.TweepError as e:
        print(f"Error posting tweet: {e}")

# Function to follow a user
def follow_user(user_handle):
    try:
        api.create_friendship(user_handle)
        print(f"Followed {user_handle}.")
    except tweepy.TweepError as e:
        print(f"Error following user: {e}")

# Function to like a tweet
def like_tweet(tweet_id):
    try:
        api.create_favorite(tweet_id)
        print("Tweet liked successfully.")
    except tweepy.TweepError as e:
        print(f"Error liking tweet: {e}")

# Main function to run the bot
def main():
    # Post a tweet
    post_tweet("Hello, this is an automated tweet from my bot!")

    # Follow a user (example: follow Twitter's official account)
    follow_user("Twitter")

    # Like a tweet (you can replace this with a real tweet ID)
    tweet_id = 1234567890123456789  # Replace with an actual tweet ID
    like_tweet(tweet_id)

    # Sleep for a while before performing other actions (to avoid rate limits)
    time.sleep(60)  # Sleep for 60 seconds to avoid hitting rate limits

if __name__ == "__main__":
    main()
