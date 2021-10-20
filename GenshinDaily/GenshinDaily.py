from GenshinDaily.classes.User import User


class GenshinDaily:

    def __init__(
            self,
            users
        ):

        self.run(users)

    def run(self, users):
        user: User
        for user in users:
            try:
                if user.reward.isClaimed():
                    print(f'\n[{user.getNickname()}] Already claimed')
                else:
                    user.reward.claimReward()
                    print(f'\n[{user.getNickname()}] Claimed {user.reward.getName()}')
            except Exception as e:
                print(f"User Instance error:\n - {e}")


def getAvailableUsers(users: list):
    for user in users:
        try:
            yield User(**user)
        except BaseException as e:
            print(f"User Instance error:\n - {e}")
