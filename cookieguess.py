import requests
import sys
from urllib3.exceptions import InsecureRequestWarning

requests.urllib3.disable_warnings()
url = sys.argv[1]
if not "https://" in url:
        url = "https://" + url
headers={'User-agent':'Mozilla//10.0',}
r = requests.get(url=url, verify=False,headers=headers)
if "server" in r.headers:
    print("server: ", r.headers["server"])
print("there are", len(r.cookies), "cookies")
#print(r.cookies.names())
print(r.cookies.values())
itemscookies = r.cookies.items()
for cookievalues in r.cookies: #prints cookies as an iteration
    print(cookievalues)

if "CSRF" in r.cookies:
    print("there are csrf tokens or values")
