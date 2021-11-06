from datetime import datetime
from typing import Union
import logging


class Logger:

    __adapterDict__: dict = {}
    __nickname__: str = None
    __rootLogger__: logging.Logger = None

    if not isinstance(__rootLogger__, logging.Logger):
        __rootLogger__ = logging.getLogger()
        logging.basicConfig(
            format='[%(asctime)s] [%(levelname)s] %(message)s',
            datefmt='%H:%M:%S',
            level=logging.INFO,
            handlers=[
                logging.FileHandler('logs/{:%Y-%m-%d[%H-%M-%S]}.log'.format(datetime.now())),
                logging.StreamHandler()
            ]
        )

    def getLogger(
        accID: str = None,
        discordWS: str = None
        ) -> Union[logging.LoggerAdapter, logging.Logger]:

        if isinstance(accID, str):
            if not isinstance(Logger.__adapterDict__.get(accID), logging.LoggerAdapter):
                logger = logging.getLogger(accID)
                logger.setLevel(logging.DEBUG)

                adapter = CustomAdapter(logger, {'psuffix': accID})
                Logger.__adapterDict__[accID] = adapter

                return adapter

            else:
                adapter = Logger.__adapterDict__[accID]

                return adapter
        else:
            return Logger.__rootLogger__

    # adapter.debug('debug message')
    # adapter.info('info message')
    # adapter.warning('warn message')
    # adapter.error('error message')
    # adapter.critical('critical message')


class CustomAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):
        return '[%s]: %s' % (self.extra['psuffix'], msg), kwargs

    def setSuffix(self, suffix):
        self.extra['psuffix'] = suffix
