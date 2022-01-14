import csv
import logging
import os
import random
import time

from prometheus_client import start_http_server

from utils import process_request

logger = logging.getLogger(__name__)


csv_file = 'results.csv'
CSV_FIELDNAMES = ['datetime', 'result']


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    if not os.path.isfile(csv_file):
        with open(csv_file, 'a', newline='') as _csvfile:
            csv.DictWriter(_csvfile, fieldnames=CSV_FIELDNAMES).writeheader()
            logger.info('Creating and writing header to CSV file because it does not exist yet')
    else:
        logger.info('CSV file already exists')

    logging.info('Starting HTTP server...')
    # Start up the server to expose the metrics.
    start_http_server(8000)

    while True:
        process_request(csv_file, CSV_FIELDNAMES)
        time.sleep(random.random())
