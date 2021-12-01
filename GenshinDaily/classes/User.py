import logging
from GenshinDaily.classes.GenshinAPI import GenshinAPI
from GenshinDaily.classes.Discord import discord
from GenshinDaily.classes.Rewards import Rewards
from GenshinDaily.classes.utils.parseAndCheckCookies import parseAndCheckCookies


class User:

    def __init__(
        self,
        cookies: str,
        webhook: str = None,
        nickname: str = None,
        avatar: str = None,
        uid: str = None
    ):
        self.cookies = parseAndCheckCookies(cookies)

        self.webhook = webhook
        self.nickname = nickname
        self.avatar = avatar
        self.uid = uid

        self.log = self.setupLogger()

        self.genshin = GenshinAPI(self.cookies, self.log)

        if self.webhook is not None:
            self.discord = discord(
                self.webhook,
                self.nickname,
                self.avatar,
                self.uid
            )

    def setupLogger(self):
        accID = self.cookies['account_id']
        extra = {'userid': self.nickname or accID}

        logger = logging.getLogger(accID)
        logger.setLevel(logging.DEBUG)

        logger = logging.LoggerAdapter(logger, extra)

        return logger

    def setupUser(self):
        self.log.info('Trying to fetch user data...')
        if self.nickname is None or self.uid is None:
            apiResponse = self.genshin.fetchUserGameInfo()
            parsed = apiResponse['data']['list'][0]
            self.uid = parsed['game_uid']
            self.nickname = parsed['nickname']

        if self.avatar is None:
            apiResponse = self.genshin.fetchUserFullInfo()
            if apiResponse['retcode'] == 0:
                self.avatar = apiResponse['data']['user_info']['avatar_url']

        self.log.extra = {'userid': self.nickname}
        self.reward = Rewards(self.genshin, self.log)

    def getNickname(self) -> str:
        return self.nickname

    def getUID(self) -> str:
        return self.uid

    def getAvatar(self) -> str:
        return self.avatar
