from datetime import datetime
from uuid import uuid4
from typing import TypedDict
from ..project_utils import strip_time_from_date

#{
# 'name': '#TheBachelor', 
# 'url': 'http://twitter.com/search?q=%23TheBachelor', 
# 'promoted_content': None, 
# 'query': '%23TheBachelor', 
# 'tweet_volume': 42242
# }
class Trend(TypedDict):
   """
      Structure of the twitter trend as they are stored in Mongo
   """
   id: str
   name: str
   url: str
   query: str
   tweet_volume: int
   created_date: datetime
   last_used_date: datetime

class TrendAggregate(TypedDict):
   id: str
   trend_id: str
   name: str
   label_1: int
   label_2: int
   label_3: int
   label_4: int
   label_5: int
   total_count: int

class DailyAggregate(TypedDict):
   id: str
   trend_id: str
   name: str
   date: datetime
   label_1: int
   label_2: int
   label_3: int
   label_4: int
   label_5: int
   total_count: int

def new_trend_dict(twitter_trend: dict):
   """
      Take in the twitter trend dictionary, filter the necessary
      fields and add the new ones
   """
   today = strip_time_from_date(datetime.utcnow())

   return {
      'id': uuid4().hex,
      'name': twitter_trend['name'],
      'url': twitter_trend['url'],
      'query': twitter_trend['query'],
      'tweet_volume': twitter_trend['tweet_volume'],
      'created_date': today,
      'last_used_date': today
   }


def new_trend_aggregate(trend: Trend) -> TrendAggregate:
   """
      Create a dictionary for the TrendAggregate model
   """
   return {
      'trend_id': trend['id'], 'name': trend['name'], 
      'label_1': 0, 'label_2': 0, 'label_3': 0,
      'label_4': 0, 'label_5': 0, 'total_count': 0,
   }

def new_daily_aggregate(trend: Trend) -> DailyAggregate:
   """
      Create a dictionary for the DailyAggregate model
   """
   return {
      'trend_id': trend['id'], 'name': trend['name'], 
      'label_1': 0, 'label_2': 0, 'label_3': 0,
      'label_4': 0, 'label_5': 0, 'total_count': 0,
      'date': datetime.utcnow(), 'tweet_volume': trend['tweet_volume'] 
   }

def update_labels(trend_aggregate: TrendAggregate, daily_aggregate: DailyAggregate, tweet_count: int):
   """
      Increment the labels of the trend aggregate with the count of the labels in the
      daily aggregate
   """
   trend_aggregate['label_1'] += daily_aggregate['label_1']
   trend_aggregate['label_2'] += daily_aggregate['label_2']
   trend_aggregate['label_3'] += daily_aggregate['label_3']
   trend_aggregate['label_4'] += daily_aggregate['label_4']
   trend_aggregate['label_5'] += daily_aggregate['label_5']
   daily_aggregate['total_count'] = tweet_count
   trend_aggregate['total_count'] += tweet_count