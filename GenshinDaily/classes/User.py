from GenshinDaily.classes.GenshinAPI import GenshinAPI
from GenshinDaily.classes.Discord import discord
from GenshinDaily.classes.Rewards import Rewards

class User:
    __slots__ = [
        "cookies",
        "webhook",
        "nickname",
        "avatar",
        "uid",
        "genshin",
        "reward"
    ]

    def __init__(
        self,
        cookies: str,
        webhook: str = None,
        avatar: str = 'https://webstatic-sea.mihoyo.com/upload/static-resource/2021/02/22/af66f7216259b9e0b49efe15feffa7dd_8822768649262579714.png',
        nickname: str = None,
        uid: str = None,
    ):

        self.cookies = cookies
        self.genshin = GenshinAPI(self.cookies)
        self.reward = Rewards(self.genshin)

        self.uid = uid
        self.nickname = nickname
        self.avatar = avatar

        self.fetchUser()

        self.webhook = webhook

        if self.webhook is not None:
            self.discord = discord(self.webhook, self.nickname, self.avatar, self.uid)
    
    def fetchUser(self):
        if self.nickname is None or self.uid is None:
            apiResponse = self.genshin.fetchUserGameInfo()
            parsed = apiResponse['data']['list'][0]
            self.uid = parsed['game_uid']
            self.nickname = parsed['nickname']

        if self.avatar is None:
            apiResponse = self.genshin.fetchUserFullInfo()
            if apiResponse['retcode'] == 0:
                self.avatar = apiResponse['data']['user_info']['avatar_url']

    def getNickname(self) -> str:
        return self.nickname

    def getUID(self) -> str:
        return self.uid

    def getAvatar(self) -> str:
        return self.avatar