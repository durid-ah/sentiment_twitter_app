from tweepy.cursor import PageIterator
import tweepy

class TwitterAPI:
   def __init__(self, settings):
      api_key = settings['apiKey']
      api_secret = settings['api_secret']

      twitter_auth = tweepy.AppAuthHandler(api_key, api_secret)
      self._trend_num = 10
      self._use_woeid = 23424977
      
      self._twitter_api = tweepy.API(
         auth_handler=twitter_auth, wait_on_rate_limit=True
      )
   
   def get_trends(self):
      """ Get USA's top 10 twitter trends """
      woeid = self._use_woeid
      num = self._trend_num
      return self._twitter_api.trends_place(woeid)[0]["trends"][:num]

   def get_n_tweets_query_iterator(self, query: str, n_pages: int) -> PageIterator:
      """ 
         Get an items iterator for the queried tweets based on the 
         n_pages (number of pages)         
      """
      return tweepy \
         .Cursor(self._twitter_api.search, q=query, count=100) \
         .pages(n_pages)