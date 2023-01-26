import azure.functions as func
import logging
import os
import fasttext

from DataCollector.data_access.repository import DataRepo
from DataCollector.import_values import import_settings
from DataCollector.trend_collector import sync_trends
from DataCollector.tweets_analyzer import analyze_tweets_for_trend
from DataCollector.twitter_handler import TwitterAPI

def load_sentiment_model() -> fasttext.FastText:
   BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   MODEL_PATH = os.path.join(BASE_DIR, 'DataCollector', 'ml_models', 'sentiment_model_q.ftz')
   return fasttext.load_model(MODEL_PATH)


def main(mytimer: func.TimerRequest) -> None:
    env_vals = import_settings()
    db_client = DataRepo(env_vals) 
    twitter_api = TwitterAPI(env_vals)
    model = load_sentiment_model()

    logging.basicConfig(
      level=logging.INFO,
      format="%(asctime)s %(levelname)s: %(message)s",
      datefmt="%y-%m-%d %H:%M:%S"
    )
   
    trends = sync_trends(twitter_api, db_client)
   
    logging.info('TRENDS TO ANALYZE:')
    for t in trends: logging.info(t['name'])
    logging.info('')

    for trend in trends:
        analyze_tweets_for_trend(trend, db_client, twitter_api, model)
