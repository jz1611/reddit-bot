# File for testing different code snippets and libraries

# import requests library for fetching data from APIs
import requests
# can us praw to simplify reddit interactions... trying to learn without it
import praw
# allow json formatting and viewing
import json
# import secret reddit info
from RedditInfo import *

test = requests.get("https://www.reddit.com/r/destinythegame/hot/.json", headers = {'User-agent': user_agent, })
# test = requests.post('https://www.reddit.com/api/submit?sr=test&title=Test', headers = {'User-agent': user_agent})
# info = test.json()["data"]["children"][:5]
with open('test.json', 'w') as file:
    json.dump(test.json(), file, sort_keys=True, indent=2)


############################################################
# Attempt with praw

# r = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
#
# sr = r.subreddit("step1")
#
# for submission in sr.hot(limit=5):
#     print(submission.title)


###########################################################
# Constantly run program?

# At the top of your code
# import time

# SECONDS_PER_MIN = 60

# def main():
    # Interval represents the interval in minutes
    # when you want your code to run
    # In this case run the bots code every 5 minutes
#     interval = 5

#     While True:

        # Your bot does stuff here
        # ...

        # Sleep x minutes before running the bot again
#         time.sleep(SECONDS_PER_MIN * interval)

# if __name__ == '__main__':
#     main()
