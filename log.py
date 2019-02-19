import logging
import os
import time

LOGS_DIR = os.environ.get('LOGS_DIR', os.path.join(os.getcwd(), 'logs'))
LOG_FILE = 'test_{}.log'.format(time.strftime("%Y%m%d-%H%M%S"))


def mkdir_p(path):
    os.makedirs(path, exist_ok=True)


logger = logging.getLogger('apt_tests')
logger.setLevel(logging.DEBUG)
# create file handler
mkdir_p(LOGS_DIR)
fh = logging.FileHandler(os.path.join(LOGS_DIR, LOG_FILE))
fh.setLevel(logging.INFO)
# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(filename)s:%(levelname)s: %(lineno)d -- %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)
