# 1 Завдання-----------------------------------------------------------
import datetime
import logging

logging.basicConfig(level = logging.INFO, filename = 'datetime.info', filemode = 'w', format = '%(asctime)s - %(levelname)s - %(message)s', datefmt = "%Y-%m-%d")
date_now = not datetime.datetime.now().strftime("%Y-%m-%d")

logging.info(f"Error{date_now}")

# 2 Завдання-----------------------------------------------------------
import logging

exception = 'An arithmetic error occurred.'

logging.basicConfig(level = logging.ERROR, filename = 'exception error', filemode = 'w')

try:
    print(10/0)
except:
    logging.exception('exception')









