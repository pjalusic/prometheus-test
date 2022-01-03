import threading

import docker
import logging
import random
import time
from prometheus_client import Summary, Gauge, start_http_server

logger = logging.getLogger(__name__)

MBFACTOR = float(1 << 20)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Create a metric to track memory usage by this container.
memory_gauge = Gauge(
    'memory_usage_in_mb',
    'Amount of memory in megabytes currently in use by this container.',
    ['name']
)

client = docker.from_env()

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request():
    res = 1 << int(random.random() * 1000000)
    logging.info(f'Res is {len(str(res))} characters long')


def some_random_stats():
    # Generate some requests.
    while True:
        process_request()

        time.sleep(random.random())


def docker_stats():
    while True:
        containers = client.containers.list()
        logger.debug(f'Found {len(containers)} container. Analyzing...')

        for container in containers:
            name = container.name

            # Get memory data for this container
            try:
                with open(f'/docker/memory/{container.id}/memory.usage_in_bytes', 'r') as memfile:
                    memory = memfile.read()
                    memory = int(memory) / MBFACTOR
                    memory_gauge.labels(name).set(memory)
                    logging.debug(f'Memory is {memory}')
            except Exception as e:
                pass
                # logger.error("Failed to update memory metric. Exception: {}".format(e))

        time.sleep(0.01)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Start up the server to expose the metrics.
    start_http_server(8000)

    threads = [
        threading.Thread(target=some_random_stats),
        threading.Thread(target=docker_stats),
    ]
    [t.start() for t in threads]
    [t.join() for t in threads]
