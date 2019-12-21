import logging, logging.config
from os import path

LOGGING_CONF_FILE_PATH = path.join(path.dirname(path.abspath(__file__)), "logging.conf")


class Logger:
    isConfigured = None

    def __init__(self, name, loggin_config_file_path=LOGGING_CONF_FILE_PATH):
        if not Logger.isConfigured:
            logging.config.fileConfig(
                fname=loggin_config_file_path, disable_existing_loggers=False
            )
            Logger.isConfigured = True

        self.logger = logging.getLogger(name)

    @staticmethod
    def get_logger(name):
        return logging.getLogger(name)

    def get_logger(self, name):
        return self.logger

    def debug(self, message, *args, **kwargs):
        """
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem", exc_info=1)
        """

        self.logger.debug(message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem", exc_info=1)
        """

        self.logger.info(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        """
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem", exc_info=1)
        """

        self.logger.warning(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info=1)
        """

        self.logger.error(message, *args, **kwargs)

    def exception(self, message, *args, **kwargs):
        """
        Convenience method for logging an ERROR with exception information.

        error(message, *args, exc_info=True,**kwargs)
        """

        self.logger.exception(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        """
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.critical("Houston, we have a %s", "major disaster", exc_info=1)
        """

        self.logger.critical(message, *args, **kwargs)
