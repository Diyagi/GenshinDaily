import requests


class GenshinAPI:

    def __init__(
        self,
        cookies: str,
    ):
        self.actid = 'e202102251931481'
        self.cookies = cookies

    def fetchUserFullInfo(self):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Origin': 'https://www.hoyolab.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.hoyolab.com/',
            'Cache-Control': 'max-age=0',
        }
        params = (
            ('gids', '2'),
        )

        response = self.fetchApiData(
            'https://api-os-takumi.mihoyo.com/community/user/wapi/getUserFullInfo',
            headers,
            params
        )

        return response

    def fetchUserGameInfo(self):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Origin': 'https://webstatic-sea.hoyolab.com',
            'Connection': 'keep-alive',
            'Referer': 'https://webstatic-sea.hoyolab.com/',
            'Cache-Control': 'max-age=0',
        }
        params = (
            ('game_biz', 'hk4e_global'),
            ('region', 'os_usa'),
        )

        response = self.fetchApiData(
            'https://api-os-takumi.mihoyo.com/binding/api/getUserGameRolesByLtoken',
            headers,
            params
        )

        return response

    def fetchReward(self):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Origin': 'https://webstatic-sea.mihoyo.com',
            'Connection': 'keep-alive',
        }

        params = (
            ('lang', 'en-us'),
            ('act_id', self.actid),
        )

        response = self.fetchApiData(
            'https://hk4e-api-os.mihoyo.com/event/sol/home',
            headers,
            params
        )

        return response

    def fetchStatus(self):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Origin': 'https://webstatic-sea.mihoyo.com',
            'Connection': 'keep-alive',
            'Referer': f'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id={self.actid}&lang=en-us',
            'Cache-Control': 'max-age=0',
        }
        params = (
            ('lang', 'en-us'),
            ('act_id', self.actid),
        )

        response = self.fetchApiData(
            'https://hk4e-api-os.mihoyo.com/event/sol/info',
            headers,
            params
        )

        return response

    def claimReward(self):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json;charset=utf-8',
            'Origin': 'https://webstatic-sea.mihoyo.com',
            'Connection': 'keep-alive',
            'Referer': f'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id={self.actid}&lang=en-us',
        }

        params = (
            ('lang', 'en-us'),
        )

        data = {
            'act_id': self.actid
        }

        response = self.postApiData(
            'https://hk4e-api-os.mihoyo.com/event/sol/sign',
            headers,
            params,
            data
        )

        return response

    def fetchApiData(self, apiLink, headers, params):
        try:
            data = requests.get(
                apiLink,
                headers=headers,
                params=params,
                cookies=self.cookies
            )
            response = data.json()

            if response['retcode'] != 0:
                if response['retcode'] == -100:
                    raise Exception('Login failed, wrong cookie ?')
                else:
                    raise Exception(f'Genshin API Retcode error: ${response}')

            return response
        except requests.exceptions.ConnectionError as e:
            raise Exception(f'API GET Connection Error: \n - {e}')
        except Exception as e:
            raise Exception(f'API GET Connection Error: \n - {e}')

    def postApiData(self, apiLink, headers, params, data=None):
        try:
            data = requests.post(
                apiLink,
                headers=headers,
                params=params,
                json=data,
                cookies=self.cookies
            )
            response = data.json()

            if response['retcode'] != 0:
                if response['retcode'] == -100:
                    raise Exception('Login failed, wrong cookie ?')
                else:
                    raise Exception(f'Genshin API Retcode error: ${response}')

            return response
        except requests.exceptions.ConnectionError as e:
            raise Exception(f'API POST Connection Error: \n - {e}')
        except Exception as e:
            raise Exception(f'API POST Connection Error: \n - {e}')
