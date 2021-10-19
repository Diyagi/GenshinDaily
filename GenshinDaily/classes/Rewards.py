from GenshinDaily.classes.GenshinAPI import GenshinAPI

class Rewards:
    
    def __init__(self, genshin: GenshinAPI):
        self.genshin = genshin
        self.parseRewards()


    def parseRewards(self):
        fetchRewardInfo = self.genshin.fetchStatus()
        fetchReward = self.genshin.fetchReward()

        self.check = fetchRewardInfo['data']['is_sign']

        if self.check: 
            self.day = fetchRewardInfo['data']['total_sign_day']-1
        else: 
            self.day = fetchRewardInfo['data']['total_sign_day']

        parsed = fetchReward['data']['awards'][self.day]

        self.icon = parsed['icon']
        self.name = parsed['name']
        self.count = parsed['cnt']

    def isClaimed(self) -> bool:
        return self.check
    
    def getName(self) -> str:
        return self.name

    def getIcon(self) -> str:
        return self.icon

    def getCount(self) -> int:
        return self.count

    def getDay(self) -> int:
        return self.day

    def claimReward(self):
        if not self.check:
            self.genshin.claimReward()