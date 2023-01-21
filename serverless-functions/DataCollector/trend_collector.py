from typing import List, Tuple
from .twitter_handler import TwitterAPI
from .data_access import DataRepo, new_trend_dict
import logging

NUM_OF_DAYS = 5

def compare_trends(api_trends, db_trends: dict) -> Tuple[List, List]:
   """
      Compare the trends retrieved from the twitter api and
      the db in order to figure out what trends need to be created in the db
      and which ones need to have their last used date updated
   """
   trends_update, trends_create = [], []
   for trend in api_trends:
      lookup_key = trend['query']
      if lookup_key in db_trends:
         update_val = db_trends[lookup_key]
         trends_update.append(update_val)
         del db_trends[lookup_key]
      else:
         t = new_trend_dict(trend)
         trends_create.append(t)

   for trend in db_trends.values():
      trends_update.append(trend)

   return trends_update, trends_create

def sync_trends(api: TwitterAPI, db: DataRepo) -> list:
   """
      Get the trends from db and twitter and merge them into a list
      of trends for analysis
   """

   # Get trends from the api and db
   logging.info('RETRIEVING DATA')
   api_trends = api.get_trends()
   db_trends = db.get_trends_for_past_n_days(NUM_OF_DAYS)

   logging.info('COMPARING THE TWO LISTS TO EACH OTHER')
   trends_to_update, trends_to_create = compare_trends(api_trends, db_trends)
   logging.info('')

   logging.info('PERSISTING THE NEW INFORMATION')
   if trends_to_create:
      logging.info('Creating trends:')
      for trend in trends_to_create: logging.info(trend['name'])
      logging.info('')
      logging.info('------------------------------------------')
      db.add_trends(trends_to_create)

   
   if trends_to_update:
      logging.info('Updating trends:')
      for trend in trends_to_update: logging.info(trend['name'])
      logging.info('------------------------------------------')
      db.update_trends_used_date(trends_to_update)


   logging.info('CONCATENATING')
   logging.info('')
   trends_to_process = trends_to_update + trends_to_create

   return trends_to_process