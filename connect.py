from pyspark import SparkContext, SQLContext
from pyspark.sql import SparkSession
import os
import pandas as pd
import praw
from pyspark.sql.types import *

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.0.1 pyspark-shell'

# spark = SparkSession.builder \
#     .config("spark.cassandra.connection.host", "10.10.5.20") \
#     .config("spark.cassandra.connection.port", 8125) \
#     .config("spark.cassandra.auth.username", "cassandra") \
#     .config("spark.cassandra.auth.password", "cassandra") \
#     .config("spark.cassandra.connection.ssl.clientAuth.enabled", True) \
#     .config("spark.cassandra.connection.ssl.enabled", True) \
#     .config("spark.cassandra.connection.ssl.keyStore.path", "/home/saque/redditfile/bigmart-client-keystore.jks") \
#     .config("spark.cassandra.connection.ssl.keyStore.password", "cassandra") \
#     .config("spark.cassandra.connection.ssl.trustStore.path",
#             "/home/saque/redditfile/generic-server-truststore.jks") \
#     .config("spark.cassandra.connection.ssl.trustStore.password", "cassandra") \
#     .config("spark.driver.extraClassPath", "/home/rocky/Music/spark-cassandra-connector_2.12:3.0.1.jar") \
#     .appName("spark-cluster") \
#     .getOrCreate()
# 
# df = spark.read \
#     .format("org.apache.spark.sql.cassandra") \
#     .option("table", "v_site") \
#     .option("keyspace", "bg") \
#     .load()

reddit = praw.Reddit(client_id="jC7HFtGfJt8g-A",  # your client id
                     client_secret="UbD5LSv13xmolzkABfDzrgOiDBFJzA",  # your client secret
                     user_agent="dev",  # user agent name
                     username="sudeep2560",  # your reddit username
                     password="sudip2560")  # your reddit password
posts = []
ml_subreddit = reddit.subreddit('nepal')
# mlsubreddit = reddit.submission("https://www.reddit.com/r/Nepal/")
# print()

for post in ml_subreddit.new(limit=50):
    df = spark.createDataFrame(
        [
            (post.id, post.author.name, int(post.created), post.num_comments,  post.selftext, str(post.subreddit), post.title, post.url)
            # create your data here, be consistent in the types.
        ],
        ["id", "author", "created", "num_comments", "selftext", "subreddit", "title", "url"]  # add your column names here
    )

df.write \
    .format("org.apache.spark.sql.cassandra") \
    .mode('append') \
    .options(table="userinfo_post", keyspace="redditdb") \
    .save()
