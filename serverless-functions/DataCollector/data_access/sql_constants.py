"""
   The SQL statements used to interract with MSSQL through pyodbc.
   The '?' represents a parameter to be passed during execution time.
"""
_TREND_COLUMNS = 'id, name, url, created_date, last_used_date, query, tweet_volume'
_TREND_AGGREGATE_COLUMNS = 'id, name, label_1, label_2, label_3, label_4, label_5, total_count, trend_id'

GET_TRENDS_TO_DATE = f"""
   SELECT {_TREND_COLUMNS}
   FROM central_backend_trend
   WHERE created_date >= ?
"""

INSERT_TREND = f"""
      INSERT INTO central_backend_trend({_TREND_COLUMNS})
      VALUES (?,?,?,?,?,?,?)
"""

UPDATE_TREND_DATE = """
   UPDATE central_backend_trend
   SET last_used_date = ?
   WHERE id = ?
"""

CREATE_TREND_AGGREGATE = f"""
   INSERT INTO central_backend_trendaggregate({_TREND_AGGREGATE_COLUMNS})
   VALUES (?,?,?,?,?,?,?,?,?)
"""

GET_TREND_AGGREGATE_BY_TREND_ID = f"""
   SELECT {_TREND_AGGREGATE_COLUMNS}
   FROM central_backend_trendaggregate
   WHERE trend_id = ?
"""

UPDATE_TREND_AGGREGATE = """
   UPDATE central_backend_trendaggregate
   SET name = ?, label_1 = ?, label_2 = ?, label_3 = ?, label_4 = ?, label_5 = ?, total_count = ?, trend_id = ?
   WHERE id = ?
"""

CREATE_DAILY_AGGREGATE = """
   INSERT central_backend_dailyaggregate(id, name, tweet_volume, label_1, label_2, label_3, label_4, label_5, total_count, date, trend_id)
   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""