# Script Author: Martin Beck
# Medium Article Follow-Along: https://medium.com/better-programming/how-to-scrape-tweets-with-snscrape-90124ed006af

# Pip install the command below if you don't have the development version of snscrape
# !pip install git+https://github.com/JustAnotherArchivist/snscrape.git

# Run the below command if you don't already have Pandas
# !pip install pandas

# Imports
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Below are two ways of scraping using the Python Wrapper.
# Comment or uncomment as you need. If you currently run the script as is it will scrape both queries
# then output two different csv files.

# Query by username
# Setting variables to be used below
maxTweets = 10000


# Creating list to append tweet data to
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('문과라서 since:2018-01-01 until:2021-09-08').get_items()):
    if i>maxTweets:
        break
    tweets_list.append([tweet.date, tweet.content])

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])


# Export dataframe into a CSV
tweets_df.to_csv('문과라서.csv', sep=',', index=False)


# Creating list to append tweet data to
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('이과라서 since:2018-01-01 until:2021-09-08').get_items()):
    if i>maxTweets:
        break
    tweets_list.append([tweet.date, tweet.content])

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])


# Export dataframe into a CSV
tweets_df.to_csv('이과라서.csv', sep=',', index=False)
