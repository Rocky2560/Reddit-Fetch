<h>Reddit Fetch </h>

In this project,the data is fetch using PRAW (Python Reddit API Wrapper) that allows for simple access to Reddit's API. For tokens of reddit, you can create it in reddit official site.The client id,client secret is provided by creating app in reddit. 

The data from reddit is fetched based on sub-reddit like nepal,linux,askreddit and many others.
Subreddit is a forum dedicated to a specific topic.

From PRAW subreddit hot posts data is fecthed from subreddit and stored in cassandra using pyspark. 
For post data consist of:

Id: post id 

Author: User name from which post is done. 

Num_comments: numbers of comments in the posts.

Created: time of post creation 

Subreddit: subreddit name 

Title: title of post 

Url: consist of Url of the post 

Self text: consist of text added in the post

And it is stored in cassandra Db.

Deployed: 10.10.5.33
Service name: reddit.service
Project directory: /home/saque/reddit

The python file connect.py has the code to fetch the reddit and store in cassandra.
