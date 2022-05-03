import logging

logger = logging.getLogger()
logger = logging.Logger("MYLOGGER")

logger.info("Logger successfully created.")
logger.log(logging.INFO, "Successful.")
logger.critical("Critical Message.")
logger.log(logging.CRITICAL, "Critical.")

for hanler in logging.root.handlers:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO)