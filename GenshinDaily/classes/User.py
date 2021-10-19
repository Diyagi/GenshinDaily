from GenshinDaily.classes.GenshinAPI import GenshinAPI
from GenshinDaily.classes.Discord import discord
from GenshinDaily.classes.Rewards import Rewards
from GenshinDaily.classes.utils.parseCookie import parseCookie


class UserSettings:

    def __init__(
            self,
            cookies: str,
            webhook: str = None,
            nickname: str = None,
            avatar: str = None,
            uid: str = None
        ):
        self.cookies = parseCookie(cookies)
        self.webhook = webhook
        self.nickname = nickname
        self.avatar = avatar
        self.uid = uid


class User:

    def __init__(
        self,
        settings: UserSettings
    ):

        self.settings = settings
        self.genshin = GenshinAPI(self.settings.cookies)
        self.reward = Rewards(self.genshin)

        self.fetchUser()

        if self.settings.webhook is not None:
            self.discord = discord(
                self.settings.webhook,
                self.settings.nickname,
                self.settings.avatar,
                self.settings.uid
            )

    def fetchUser(self):
        if self.settings.nickname is None or self.settings.uid is None:
            apiResponse = self.genshin.fetchUserGameInfo()
            parsed = apiResponse['data']['list'][0]
            self.settings.uid = parsed['game_uid']
            self.settings.nickname = parsed['nickname']

        if self.settings.avatar is None:
            apiResponse = self.genshin.fetchUserFullInfo()
            if apiResponse['retcode'] == 0:
                self.settings.avatar = apiResponse['data']['user_info']['avatar_url']

    def getNickname(self) -> str:
        return self.settings.nickname

    def getUID(self) -> str:
        return self.settings.uid

    def getAvatar(self) -> str:
        return self.settings.avatar
