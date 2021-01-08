import praw
import pdb
import re
import os

reddit = praw.Reddit('KAbot', user_agent='KAbot 0.1')
subreddit = reddit.subreddit('pythonforengineers')

#     print('Title', submissions.title)
#     print('selftext', submissions.selftext)
#     print('score', submissions.score)
#     print('\n \n \n \n \n')

if not os.path.isfile('posts_replied_to.txt'):
    posts_replied_to = []
else: 
    with open('posts_replied_to.txt', 'r') as f:
        post_replied_to = f.read()
        post_replied_to = post_replied_to.split('\n') 
        post_replied_to = list(filter(None, post_replied_to))
    
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search('i love python', submission.title, re.IGNORECASE):
            submission.reply('Botty bot says: Me Too!')

