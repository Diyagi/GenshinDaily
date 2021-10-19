class discord: 

    def __init__(
        self,
        webhook: str,
        nickname: str,
        avatar: str,
        uid: str,
    ):

        self.webhook = webhook
        self.nickname = nickname
        self.avatar = avatar
        self.uid = uid