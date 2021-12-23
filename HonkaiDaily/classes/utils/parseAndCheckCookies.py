def parseAndCheckCookies(cookies: str):
    loadedCookies = {}
    for cookiedata in cookies.split("; "):
        d1, d2 = cookiedata.split("=", 1)
        loadedCookies[d1] = d2

    if loadedCookies.get('_MHYUUID') is None\
        or loadedCookies.get('ltoken') is None\
        or loadedCookies.get('ltuid') is None\
        or loadedCookies.get('cookie_token') is None\
        or loadedCookies.get('account_id') is None\
        or loadedCookies.get('mi18nLang') is None:

        raise BaseException('Incomplete Cookies !')
    else:
        return loadedCookies
