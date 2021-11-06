from GenshinDaily.classes.Logger import Logger
from GenshinDaily.classes.User import User


class GenshinDaily:

    def __init__(
            self,
            users
        ):
        self.logger = Logger.getLogger()
        self.run(users)

    def run(self, users):
        user: User
        for user in users:
            try:
                if user.reward.isClaimed():
                    user.log.info('Already claimed\n')
                else:
                    user.reward.claimReward()
                    user.log.info(f'Claimed {user.reward.getName()}\n')
            except Exception as e:
                print(f"User Instance error:\n - {e}")


def getAvailableUsers(users: list):
    logger = Logger.getLogger()
    for user in users:
        try:
            yield User(**user)
        except Exception as e:
            logger.error(f'{e}\n')
