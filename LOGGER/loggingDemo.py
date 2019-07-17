# import logging
# logging.basicConfig(filename="test.log",
#                     level=logging.DEBUG,
#                     format='%(asctime)s: %(levelname)s: %(message)s',
#                     datefmt='%d/%m/%y %I/%M/%S %p'
#                     )
# logging.debug("This is the debug message")
# logging.info("This is the info message")
# logging.warning("This is the warning message")
# logging.error("This is the error message")
# logging.critical("This is the critical message")
import logging
logging.basicConfig(filename="test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%y %I/%M/%S %p',filemode='a'
                    )
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is the debug message")
logger.info("This is the info message")
logger.warning("This is the warning message")
logger.error("This is the error message")
logger.critical("This is the critical message")
