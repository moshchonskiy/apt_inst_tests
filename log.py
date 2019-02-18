import logging
import os
import time

LOGS_DIR = os.environ.get('LOGS_DIR', os.getcwd() + "/logs")


def generate_time():
    return time.strftime("%Y%m%d-%H%M%S")


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s %(filename)s:'
                    '%(lineno)d -- %(message)s',
                    filename=os.path.join(LOGS_DIR, 'test_{}.log'.format(generate_time())),
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s %(filename)s:'
                              '%(lineno)d -- %(message)s')
console.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(console)
