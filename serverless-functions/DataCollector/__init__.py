import datetime
import logging
import os

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    # utc_timestamp = datetime.datetime.utcnow().replace(
    #     tzinfo=datetime.timezone.utc).isoformat()

    # if mytimer.past_due:
    #     logging.info('The timer is past due!')

    # logging.info('Python timer trigger function ran at %s', utc_timestamp)
    logging.info('DURID ENVIRONMENT VALUE: %s', os.environ['api_key'])
