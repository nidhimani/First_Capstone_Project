
# importing the required modules
from pymongo import MongoClient
import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime as datetime
import streamlit as st
0
st.title("Scrapping Data Using Twitter")   # Setting the title of the page 

with st.form("Twitter_Scrapping"):
 from_keyword = st.text_input("Enter the domain of interests for viewing tweets with hashtag(#)")
 # giving input dates to display the tweets
 start = st.date_input("Enter the starting date to display tweets", datetime.date(2022,1,1))
 end = st.date_input("Enter the end date to display tweets", datetime.date(2023,1,1))
 data = f'"(from:{from_keyword}) since:{start} until:{end}"'
 tweets_count = st.slider("Number of tweets to be displayed ?",0,500)
 submitted = st.form_submit_button("Submit")

 list = []
 for i,tweet in enumerate(sntwitter.TwitterSearchScraper(data).get_items()):
  if len(list) == tweets_count:
           break
  list.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.lang , tweet.source, tweet.likeCount])
 df = pd.DataFrame(list, columns = ['Datetime', 'Tweet Id','Tweet_url', 'Text', 'Username', 'Reply_count', 'Retweet_count','Tweet_lang','Source','Like_count'])
 submit = print(df)
 st.dataframe(df)
       

# storing data in a database    
if st.button("Store the scrapped_data in a data_base"):
   client = MongoClient("mongodb://localhost:27017")
   db = client["Final1"]
   new_collection = db["data"]
   import json
   json_file = df.to_json()
   file = json.loads(json_file)
   for i in json.loads(json_file):
     file = json.loads(json_file)
     new_collection.insert_one(file)
     
     
# saving the scrapped data into a csv file         
csv = df.to_csv()
st.download_button("Download data as CSV",
                      csv,
                      file_name='large_df.csv'
                      )

# saving the scrapped data into a json file
json_file = df.to_json()
st.download_button("Download data as json_file",
                  json_file,
                  file_name='large_df.json',
                  )

    
 
