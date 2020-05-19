import logging


logger = logging.getLogger()
# logger.setLevel()

logger1 = logging.getLogger('my first logger')
logger1.setLevel(logging.WARNING)

file_handler = logging.FileHandler('test.log')
console_handler = logging.StreamHandler()
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formater)
console_handler.setFormatter(formater)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger1.addHandler(
    file_handler
)
logger1.addHandler(console_handler)

logger.info('this is info')
logger1.info('this is info of logger1')