import logging
import os

class LogGen:
    @staticmethod
    def loggen():

        if not os.path.exists("./Logs"):
            os.makedirs("./Logs")

        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

