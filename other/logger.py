import logging


def get_logger() -> logging:
    logger = logging.getLogger(__name__)
    f_handler = logging.FileHandler('../file.log')
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.ERROR)
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
    f_handler.setFormatter(f_format)
    c_handler.setFormatter(c_format)
    logger.addHandler(f_handler)
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)
    return logger
