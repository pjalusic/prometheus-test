from prometheus_client import start_http_server, Summary, Gauge
import random
import time

g = Gauge('some_test_metric', 'TEST METRIC')


def test_gauge():
    x = random.random()
    return x


g.set_function(lambda: test_gauge())

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
