from typing import List
import pymssql
from datetime import datetime
from .sql_constants import \
   GET_TRENDS_TO_DATE, INSERT_TREND, UPDATE_TREND_DATE, CREATE_TREND_AGGREGATE, \
   GET_TREND_AGGREGATE_BY_TREND_ID, UPDATE_TREND_AGGREGATE, CREATE_DAILY_AGGREGATE
from ..project_utils import get_datetime_from_n_days_ago
from uuid import uuid4
from .models import Trend, TrendAggregate, DailyAggregate

class DataRepo:
   def __init__(self, settings: dict):
      server = settings['DB_HOST']
      username = settings['DB_USERNAME']
      password = settings['DB_PASSWORD']
      database = 'sentiment_app'
      self.conn = pymssql.connect(host=server, port=1433, user=username, password=password, database=database)
   
   def get_trends_for_past_n_days(self, n_days: int) -> dict:
      """
         Get the trends for the last n_days and return a dictionary where
         the trend's query field is the key
      """
      day = get_datetime_from_n_days_ago(n_days)
      cursor = self.conn.cursor()
      cursor.execute(GET_TRENDS_TO_DATE, day)
      result = dict(map(lambda t: (t[5], to_trend_dict_from_sql_row(t)), cursor))
      cursor.close()
      return result


   def update_trends_used_date(self, trends: list):
      """
         Update the trends last_used_date with the current date
      """
      cursor = self.conn.cursor()
      for trend in trends:
         cursor.execute(UPDATE_TREND_DATE, (datetime.utcnow(), trend['id']))
      self.conn.commit()


   def add_trends(self, trends: List[dict]):
      """Insert a list of trends into their collection"""
      cursor = self.conn.cursor()

      for trend in trends:
         cursor.execute(
            INSERT_TREND, (trend['id'], trend['name'], trend['url'],
            trend['created_date'], trend['last_used_date'],
            trend['query'], trend['tweet_volume']) 
         )

      self.conn.commit()


   def create_trend_aggregate(self, trend_aggregate: TrendAggregate):
      cursor = self.conn.cursor()
      
      cursor.execute(
         CREATE_TREND_AGGREGATE, (uuid4().hex, trend_aggregate['name'],
         trend_aggregate['label_1'], trend_aggregate['label_2'], trend_aggregate['label_3'],
         trend_aggregate['label_4'], trend_aggregate['label_5'], trend_aggregate['total_count'],
         trend_aggregate['trend_id'])
      )

      self.conn.commit()


   def get_aggregate_by_trend_id(self, trend_id: str) -> TrendAggregate:
      cursor = self.conn.cursor()
      
      cursor.execute(GET_TREND_AGGREGATE_BY_TREND_ID, trend_id)
      aggregate_row = cursor.fetchone()
      
      return to_trend_aggregate_from_sql_row(aggregate_row)

   def update_trend_aggregate(self, trend_aggregate: TrendAggregate):
      cursor = self.conn.cursor()
      
      cursor.execute(UPDATE_TREND_AGGREGATE, (trend_aggregate['name'],
      trend_aggregate['label_1'], trend_aggregate['label_2'], trend_aggregate['label_3'],
      trend_aggregate['label_4'], trend_aggregate['label_5'], trend_aggregate['total_count'],
      trend_aggregate['trend_id'], trend_aggregate['id']))

      self.conn.commit()

   def create_daily_aggregate(self, daily_aggregate: DailyAggregate):
      cursor = self.conn.cursor()

      cursor.execute(CREATE_DAILY_AGGREGATE, (uuid4().hex, daily_aggregate['name'],
      daily_aggregate['tweet_volume'], daily_aggregate['label_1'],
      daily_aggregate['label_2'], daily_aggregate['label_3'],
      daily_aggregate['label_4'], daily_aggregate['label_5'],
      daily_aggregate['total_count'], daily_aggregate['date'], daily_aggregate['trend_id']))
      
      self.conn.commit()


### Helpers:
def to_trend_dict_from_sql_row(trend_row: tuple) -> Trend:
   """
      Convert the sql row into a Trend dictionary
   """
   return {
      'id': trend_row[0],
      'name': trend_row[1],
      'url': trend_row[2],
      'query': trend_row[5],
      'tweet_volume': trend_row[6],
      'created_date': trend_row[3],
      'last_used_date': trend_row[4]
   }


def to_trend_aggregate_from_sql_row(aggregate_row: tuple) -> TrendAggregate:
   if aggregate_row is None:
      return None

   return {
      'id': aggregate_row[0],
      'name': aggregate_row[1],
      'label_1': aggregate_row[2],
      'label_2': aggregate_row[3],
      'label_3': aggregate_row[4],
      'label_4': aggregate_row[5],
      'label_5': aggregate_row[6],
      'total_count': aggregate_row[7],
      'trend_id': aggregate_row[8]
   }
