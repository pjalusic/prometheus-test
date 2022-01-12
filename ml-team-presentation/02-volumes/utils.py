import csv
import logging
import random
from datetime import datetime

from prometheus_client import Summary

logger = logging.getLogger(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(csv_file, CSV_FIELDNAMES):
    res = 2 ** int(random.random() * 1000000)
    res = len(str(res))

    data = {
        'datetime': datetime.utcnow().isoformat(),
        'result': res
    }
    with open(csv_file, 'a', newline='') as _csvfile:
        csv.DictWriter(_csvfile, fieldnames=CSV_FIELDNAMES).writerow(data)

    logger.info(f'Res is {res} characters long. Writing to CSV')
