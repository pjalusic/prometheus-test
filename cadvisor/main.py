import logging
import random
import threading
import time
from prometheus_client import Summary
from prometheus_client.exposition import start_http_server

logger = logging.getLogger(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
HEAVY_REQUEST_TIME = Summary('request_heavy_processing_seconds', 'Time spent processing heavy request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request():
    res = 1 << int(random.random() * 1000000)
    logging.info(f'Res1 is {len(str(res))} characters long')


def some_random_stats():
    # Generate some requests.
    while True:
        process_request()
        time.sleep(random.random())


@HEAVY_REQUEST_TIME.time()
def generate_heavy_load():
    res = 2 ** int(random.random() * 3000000)
    logging.info(f'Res2 is {len(str(res))} characters long')


def some_other_random_stats():
    # Generate some requests.
    while True:
        generate_heavy_load()
        time.sleep(random.random())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Start up the server to expose the metrics.
    start_http_server(8000)

    threads = [
        threading.Thread(target=some_random_stats),
        threading.Thread(target=some_other_random_stats),
    ]
    [t.start() for t in threads]
    [t.join() for t in threads]
