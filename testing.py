# File for testing different code snippets and libraries

# import requests library for fetching data from APIs
import requests
import praw
from RedditInfo import *

# test = requests.get("https://www.reddit.com/r/learnPython/hot/.json")

r = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

sr = r.subreddit("learnpython")

for submission in sr.hot(limit=5):
    print(submission.author)
