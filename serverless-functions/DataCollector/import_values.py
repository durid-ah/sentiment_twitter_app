import os

def import_settings() -> dict:
   return {
      'api_key' : os.environ['api_key'],
      'api_secret' : os.environ['api_secret'],
      'DB_HOST' : os.environ['DB_HOST'],
      'DB_USERNAME' : os.environ['DB_USERNAME'],
      'DB_PASSWORD' : os.environ['DB_PASSWORD'],
   }