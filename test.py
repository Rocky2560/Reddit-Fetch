import pandas as pd
import praw
from praw.reddit import Comment

reddit = praw.Reddit(client_id="jC7HFtGfJt8g-A",  # your client id
                     client_secret="UbD5LSv13xmolzkABfDzrgOiDBFJzA",  # your client secret
                     user_agent="dev",  # user agent name
                     username="sudeep2560",  # your reddit username
                     password="sudip2560")  # your reddit password
posts = []
ml_subreddit = reddit.subreddit('nepal+linux')
for post in ml_subreddit.hot(limit=None):
    posts.append(
        [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
# posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
# print(posts)
# stream = praw.helpers.comment_stream("nepal+linux", limit=None)
for comment in reddit.subreddit('nepal').stream.comments():
    # print(type(comment))
    # Comment.parent()
    # for key in comment:
    #     print(key,comment[key])
    if comment.is_root:
        # print(comment.body)
        # print(comment.parent())
        # print(comment.parent)
        # print(comment.is_root)
        print(comment.id)
    # print(comment.id)
    # print(comment.author)
