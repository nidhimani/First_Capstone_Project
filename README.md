# First_Capstone_Project
Twitter_Scrapping
# Zen_Project
*snscrape*

snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.

*I am going to use  on twitter:*
Twitter: users, user profiles, hashtags, searches, tweets (single or surrounding thread), list posts, and trends


*streamlit-twitter-scraper*

*Requirements*

snscrape requires Python 3.8 or higher. The Python package dependencies are installed automatically when you install snscrape.

. Snscrape

. Streamlit

. pandas

*Installation*

 #Install Snscraper
 
#A Scraper for social network is called Snscraper

>>pip install snscrape

 '#Now creating a GUI using streamlit'
'#install streamlit libreray'

>>pip install streamlit

*#Import Requirements*

 import streamlit as st
 
 import snscrape.modules.twitter as sntwitter
 
 import pandas pd
 
 *using the following query format*
 
 The query must be specified as a Python dictionary containing a list of fields
 
 
 >>(from:{Content}) until:{until_date} since:{Since_date}
 
 *until*
 
This parameter refers to the maximum allowed date. It has to be specified in the YYYY-MM-DD format.

*since*

This parameter refers to the minimum allowed date. It has to be specified in the YYYY-MM-DD format.
  
*After adding the required attributes in tweet_list i am saving in a dataframe*

>>df = pd.DataFrame(tweets_list(, columns=["give the column names"])

*Update the file in your Database*


        client = MongoClient('username:password')
        
        db = client.Tweets_database
        
        collection = db.twitter_collection
        
        tweet_data = df.to_dict("records")


        collection.insert_many(tweet_data)

*#Now creating a GUI using streamlit*

create a streamlit project in bye using st.form(key="give name")

>>Run the same code in streamlit form by using streamlit input varibles

*Download the retrive file*

>>st.download_button("Download CSV",
                       df.to_csv(),
                       file_name = f'{file_name}',
                       mime="text/csv")
                       
                       
*Update in database by adding Mongo_DB credentials and create update button*

>>if st.form_submit_button(label='Update')

>>Update = collection.insert_many("your database name")

*run the streamlit*

>>streamlit run main.py
