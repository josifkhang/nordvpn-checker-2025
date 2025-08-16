# <coded by josif>
# Contact  : +8801868608046 (Whatsapp)
# Github   : https://github.com/josifkhang/nordvpn-login-api
# Telegram : t.me/josifkhan
# -----------------------------------------------------------------------
import requests
class NORDVPN:
	def login(selfy,user,password,proxy_url):
		with requests.Session() as session:
			url = "https://nordvpn.josiftools.com/nordlogin"
			params = {
				"user": "trejohninvestments@gmail.com",
				"pass": "trej4049",
				"proxies": proxy_url #optional but recommended
			}
			try:
				response = session.get(url, params=params, timeout=10)
				print("Response Text:", response.json())
				# return response.json()
			except requests.exceptions.RequestException as e:print("Error:", e)
# -----------------------------------------------------------------------
email     = "user_email@josiftools.com"
password  = "user_pass"
proxy_url = "http://username:password@host:port" # http or socks5
# -----------------------------------------------------------------------
nd = NORDVPN()
nd.login(user=email,password=password,proxy_url=proxy_url)

# -----------------------------------------------------------------------
# ✅NOTICE: THIS API HAS LIMIT, IF U R INTERESTED IN SOURCE CODE YOU CAN CONTACT ME.

