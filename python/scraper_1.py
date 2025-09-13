import requests
import tweepy
import os
from textblob import TextBlob

# ========================================================================
# This script scrapes recent tweets and Facebook page posts related to
# ocean hazards using the official Twitter API v2 and Facebook Graph API,
# and then performs sentiment analysis on the retrieved content.
#
# Before running this script, you MUST get your own API credentials and
# install the required libraries:
# pip install tweepy requests textblob
#
# - For Twitter: Create a developer account and get a Bearer Token.
# - For Facebook: Create a developer account, a Facebook App, and get
#   a Page Access Token and the Page ID you want to scrape.
# ========================================================================


# === Twitter API v2 setup ===
# Replace this placeholder with your actual Twitter Bearer Token
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN", "AAAAAAAAAAAAAAAAAAAAAOnS3wEAAAAAAYVNy0cKH%2FdLmyZIfNFs76Y%2BPmI%3Dd7TFqbMScFTpvyrg7oxvDQ0VrFgtuKhyweointfslpbAGifWnq")

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text and returns a label.
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def search_tweets_by_keywords(keywords, max_results=10):
    """
    Searches for recent tweets containing any of the given keywords
    and analyzes their sentiment.
    """
    client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
    # Build query string with OR between keywords, e.g. "tsunami OR hurricane OR cyclone"
    query = " OR ".join(keywords) + " -is:retweet lang:en"  # exclude retweets, English only
    
    try:
        tweets = client.search_recent_tweets(query=query, max_results=max_results)
        if not tweets.data:
            print("No tweets found for the given keywords.")
            return []
        
        results = []
        for tweet in tweets.data:
            sentiment = analyze_sentiment(tweet.text)
            results.append({'text': tweet.text, 'sentiment': sentiment})
        return results
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []

# === Facebook Graph API setup ===
# Replace these placeholders with your actual Facebook credentials
FACEBOOK_ACCESS_TOKEN = 'YOUR_FACEBOOK_ACCESS_TOKEN'
FACEBOOK_PAGE_ID = 'YOUR_FACEBOOK_PAGE_ID'

def get_facebook_page_posts_filtered(page_id, access_token, keywords, limit=25):
    """
    Fetches posts from a public Facebook page, filters them by keywords,
    and analyzes their sentiment.
    """
    url = f"https://graph.facebook.com/v15.0/{page_id}/posts"
    params = {
        'access_token': access_token,
        'limit': limit,
        'fields': 'message,created_time'  # fetch message and timestamp
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        posts = data.get('data', [])

        filtered_posts = []
        for post in posts:
            message = post.get('message', '')
            if any(keyword.lower() in message.lower() for keyword in keywords):
                sentiment = analyze_sentiment(message)
                filtered_posts.append({'message': message, 'sentiment': sentiment})
        return filtered_posts
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Facebook posts: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    # Define ocean hazard keywords
    ocean_hazards = ["tsunami", "hurricane", "cyclone", "storm surge", "rip current", "rogue wave"]

    # Twitter keyword search and sentiment analysis
    print("Recent tweets containing ocean hazard keywords:")
    tweets = search_tweets_by_keywords(ocean_hazards, max_results=10)
    for tweet in tweets:
        print(f"- [Sentiment: {tweet['sentiment']}] {tweet['text']}")

    # Facebook page posts filtered by keywords and sentiment analysis
    print(f"\nRecent Facebook posts from page ID {FACEBOOK_PAGE_ID} containing ocean hazard keywords:")
    fb_posts = get_facebook_page_posts_filtered(FACEBOOK_PAGE_ID, FACEBOOK_ACCESS_TOKEN, ocean_hazards, limit=25)
    for post in fb_posts:
        print(f"- [Sentiment: {post['sentiment']}] {post['message']}")
