import datetime
import logging
from tornado.log import LogFormatter
from GenshinDaily.classes.User import User
from GenshinDaily.classes.utils.createDirifNotExists import createDir


class GenshinDaily:

    def __init__(
            self,
            users
        ):
        self.logger = self.setupLogger()
        self.run(users)

    def run(self, users):
        user: User
        for user in users:
            try:
                self.logger.info('Trying to setup new user...')
                user.setupUser()
                if user.reward.isClaimed():
                    user.log.info('Already claimed\n')
                else:
                    user.reward.claimReward()
                    user.log.info(f'Claimed {user.reward.getName()}\n')
            except Exception as e:
                user.log.critical(f"User Instance error:\n - {e}", exc_info=0)
                user.log.debug("", exc_info=1)

    def setupLogger(self) -> logging.Logger:
        logger: logging.Logger = logging.getLogger()

        if createDir('./logs'):
            logger.debug('Created Logs dir.')

        datefmt = "%m-%d %H:%M:%S"
        fmt = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d %(userid)s]%(end_color)s %(message)s"

        trndStdFormatter = LogFormatter(
            datefmt=datefmt,
            fmt=fmt
        )

        trndFileFormatter = LogFormatter(
            datefmt=datefmt,
            fmt=fmt,
            color=False
        )

        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(trndStdFormatter)

        today = datetime.datetime.now()
        file_handler = logging.FileHandler('./logs/{}.log'.format(today.strftime('%Y-%m-%d[%H-%M-%S]')))
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(trndFileFormatter)

        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)

        return logger
