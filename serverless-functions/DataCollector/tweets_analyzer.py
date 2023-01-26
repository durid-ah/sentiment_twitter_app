from DataCollector.data_access.models import TrendAggregate, new_daily_aggregate, new_trend_aggregate, update_labels
from DataCollector.data_access.repository import DataRepo
from .twitter_handler import TwitterAPI
from .project_utils import get_datetime_from_n_days_ago, strip_down_comment
from fasttext import FastText
import logging

label_map = {
   '__label__1': 'label_1',
   '__label__2': 'label_2',
   '__label__3': 'label_3',
   '__label__4': 'label_4',
   '__label__5': 'label_5'
}

def convert_label(label: str):
   return label_map[label]

def create_or_increment_count(label: str, sentiment_count: dict):
   """
      Check if a dictionary has a certain label and increment its 
   """
   label = convert_label(label)
   if label in sentiment_count:
      sentiment_count[label] += 1
   else:
      sentiment_count[label] = 1


def analyze_tweets_for_trend(
   trend, db_client: DataRepo, twitter_api: TwitterAPI, model: FastText
):
   logging.info(f'Starting Analysis For: {trend["name"]}')
   logging.info('Initializing Process') 
   query = trend['query']
   pages = twitter_api.get_n_tweets_query_iterator(query, 3)
   yesterday = get_datetime_from_n_days_ago(1)
   trend_aggregate: TrendAggregate = db_client.get_aggregate_by_trend_id(trend['id'])
   daily_aggregate = new_daily_aggregate(trend)
   tweet_count = 0
   is_new_trend = False

   if trend_aggregate is None:
      is_new_trend = True
      trend_aggregate = new_trend_aggregate(trend)

   logging.info('Iterating through tweets') 
   
   for page in pages:
      for status in page:
         created_date = status.created_at.replace(tzinfo=None) 
         if created_date <= yesterday:
            break
         else:
            tweet_count += 1
            cleaned_text = strip_down_comment(status.text) 
            prediction = model.predict(cleaned_text)
            label: str = prediction[0][0]
            create_or_increment_count(label, daily_aggregate)

   logging.info('Updating aggregates') 
   update_labels(trend_aggregate, daily_aggregate, tweet_count)

   logging.info('Persisting')
   if is_new_trend:
      db_client.create_trend_aggregate(trend_aggregate)
   else:
      db_client.update_trend_aggregate(trend_aggregate)

   db_client.create_daily_aggregate(daily_aggregate)
   