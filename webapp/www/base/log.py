import logging

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.INFO


class Logger(object):
    """
    封装好的Logger工具
    """

    def __init__(self, logPath):
        """
        initial
        """
        log_path = logPath
        logging.basicConfig(level=LOG_LEVEL,
                            format=FORMAT,
                            datefmt="%Y-%m-%d %H:%M:%S",
                            filename=log_path,
                            filemode="a")
        console = logging.StreamHandler()
        console.setLevel(LOG_LEVEL)
        formatter = logging.Formatter(FORMAT)
        console.setFormatter(formatter)
        logging.getLogger("").addHandler(console)

    def debug(self, msg=""):
        """
        output DEBUG level LOG
        """
        logging.debug(str(msg))

    def info(self, msg=""):
        """
        output INFO level LOG
        """
        logging.info(str(msg))

    def warning(self, msg=""):
        """
        output WARN level LOG
        """
        logging.warning(str(msg))

    def exception(self, msg=""):
        """
        output Exception stack LOG
        """
        logging.exception(str(msg))

    def error(self, msg=""):
        """
        output ERROR level LOG
        """
        logging.error(str(msg))

    def critical(self, msg=""):
        """
        output FATAL level LOG
        """
        logging.critical(str(msg))

logger = Logger('./webapp.log')
