from GenshinDaily.classes.User import User
from GenshinDaily.classes.utils.parseCookie import parseCookie

class GenshinDaily:
	__slots__ = [
		"cookie",
		"webhook",
		"avatar",
		"nickname",
		"uid",
		"user"
	]

	def __init__(
			self,
			cookie: str,
			webhook: str = None,
			avatar: str = None,
			nickname: str = None,
			uid: str = None
		) -> None:

		self.cookie = parseCookie(cookie)

		self.user = User(self.cookie, webhook, avatar, nickname, uid)
		self.tryClaim()

	def tryClaim(self):
		if self.user.reward.isClaimed():
			print('Already claimed')
		else:
			self.user.reward.claimReward()