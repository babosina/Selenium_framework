import inspect
import logging


def custom_logger(log_level=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # if console_level != None:
    #     ch = logging.StreamHandler()  # Streamhandler logs to console
    #     ch.setLevel(console_level)
    #     ch_format = logging.Formatter('%(asctime)s - %(message)s')
    #     ch.setFormatter(ch_format)
    #     logger.addHandler(ch)

    fh = logging.FileHandler('{}.log'.format(logger_name))
    fh.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
