"""
   The SQL statements used to interract with MSSQL through pyodbc.
   The '%s' and '%d' represent the parameters to be passed during execution time.
"""
_TREND_COLUMNS = 'id, name, url, created_date, last_used_date, query, tweet_volume'
_TREND_AGGREGATE_COLUMNS = 'id, name, label_1, label_2, label_3, label_4, label_5, total_count, trend_id'

GET_TRENDS_TO_DATE = f"""
   SELECT {_TREND_COLUMNS}
   FROM twitter_trend
   WHERE created_date >= %s
"""

INSERT_TREND = f"""
   INSERT INTO twitter_trend({_TREND_COLUMNS})
   VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

UPDATE_TREND_DATE = """
   UPDATE twitter_trend
   SET last_used_date = %s
   WHERE id = %s
"""

CREATE_TREND_AGGREGATE = f"""
   INSERT INTO trend_aggregate({_TREND_AGGREGATE_COLUMNS})
   VALUES (%s, %s, %d, %d, %d, %d, %d, %d, %s)
"""

GET_TREND_AGGREGATE_BY_TREND_ID = f"""
   SELECT {_TREND_AGGREGATE_COLUMNS}
   FROM trend_aggregate
   WHERE trend_id = %s
"""

UPDATE_TREND_AGGREGATE = """
   UPDATE trend_aggregate
   SET name = %s, label_1 = %d, label_2 = %d, label_3 = %d, label_4 = %d, label_5 = %d, total_count = %d, trend_id = %s
   WHERE id = %s
"""

CREATE_DAILY_AGGREGATE = """
   INSERT trend_daily_aggregate(id, name, tweet_volume, label_1, label_2, label_3, label_4, label_5, total_count, date, trend_id)
   VALUES (%s, %s, %d, %d, %d, %d, %d, %d, %d, %s, %s)
"""