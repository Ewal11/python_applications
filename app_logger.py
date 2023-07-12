import logging
from schemas import LogConfiguration


def get_logger():
    logger = logging.getLogger(LogConfiguration.logger_name)
    formatter = logging.Formatter(LogConfiguration.logger_formatter)
    handler = logging.FileHandler(filename=LogConfiguration.log_file_base_name)
    handler.setFormatter(formatter)
    logger.setLevel('INFO')
    logger.addHandler(handler)
    return logger


ap_logger = get_logger()
