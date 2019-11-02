import logging

logger = logging.getLogger('logger_before_request')


def logger_before_request():
    logger.info('before_request')
