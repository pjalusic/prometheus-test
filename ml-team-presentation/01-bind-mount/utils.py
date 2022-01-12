import logging
import random
from prometheus_client import Summary

logger = logging.getLogger(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request():
    res = 2 ** int(random.random() * 2000000)
    logger.info(f'Res is {len(str(res))} characters long')
