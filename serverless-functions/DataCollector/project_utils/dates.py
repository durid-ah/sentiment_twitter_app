import datetime as dt
from datetime import datetime


def strip_time_from_date(today: datetime) -> datetime:
   return today.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

def get_datetime_from_n_days_ago(n_days: int) -> datetime:
   today = datetime.utcnow()
   up_to_date = today - dt.timedelta(days=n_days)
   return strip_time_from_date(up_to_date)