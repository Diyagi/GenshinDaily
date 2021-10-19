from GenshinDaily.classes.User import User


class GenshinDaily:

    def __init__(
            self,
            usersSettings: list = []
        ):

        self.run(usersSettings)

    def run(self, usersSettings: list = []):
        for userSetting in usersSettings:
            try:
                user = User(userSetting)
                if user.reward.isClaimed():
                    print(f'[{user.getNickname()}] Already claimed')
                else:
                    user.reward.claimReward()
                    print(f'[{user.getNickname()}] Claimed {user.reward.getName()}')
            except Exception as e:
                print(f"User Instance error:\n - {e}")
