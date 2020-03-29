# File for testing different code snippets and libraries

# import requests library for fetching data from APIs
import requests
import praw
import json
from RedditInfo import *

test = requests.get("https://www.reddit.com/r/destinythegame/hot/.json", headers = {'User-agent': user_agent})
info = test.json()["data"]["children"][:5]
with open('test.json', 'w') as file:
    json.dump(info, file, indent=2)



# r = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
#
# sr = r.subreddit("step1")
#
# for submission in sr.hot(limit=5):
#     print(submission.title)
