import logging
import random
import time

from prometheus_client import start_http_server

from utils import process_request


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # logging.info('Starting HTTP server...')

    # Start up the server to expose the metrics.
    start_http_server(8000)

    while True:
        process_request()
        time.sleep(random.random())
