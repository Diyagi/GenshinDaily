def parseCookie(cookies: str):
	loadedCookies = {}
	for cookiedata in cookies.split("; "):
		d1, d2 = cookiedata.split("=", 1)
		loadedCookies[d1] = d2
	return loadedCookies