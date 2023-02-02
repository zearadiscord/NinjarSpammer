import requests, re, random, string


def randomstring():
  randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]
  return ''.join(randlst)


user = input("Username > ")
message = input("Message > ")
client = requests.Session()
r = client.get(f"https://www.ninjar.jp/users/{user}/themes/new")
c = re.findall('"csrf-token" content=".+"', r.text)[0].split('"')[3]
print("[+] Got Token: " + c)
cookie =  r.headers["Set-Cookie"]

headers = {
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "ja-JP,ja;q=0.9,en;q=0.8",
  "cache-control": "no-cache",
  "content-type": "application/x-www-form-urlencoded",
  "cookie": cookie,
  "origin": "https://www.ninjar.jp",
  "pragma": "no-cache",
  "referer": f"https://www.ninjar.jp/users/{user}/themes/new",
  "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": '"Windows"',
  "sec-fetch-dest": "document",
  "sec-fetch-mode": "navigate",
  "sec-fetch-site": "same-origin",
  "sec-fetch-user": "?1",
  "upgrade-insecure-requests": "1",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
data = {
  "authenticity_token": c,
  "theme_form[title]": message+" - "+randomstring(),
  "theme_form[redirect_url]": "",
  "commit": "匿名で質問を送る"
}

r2 = client.post(f"https://www.ninjar.jp/users/{user}/themes",
                 data=data,
                 allow_redirects=True)
if r2.status_code == 200:
  print("[+] SendedMessage")
else:
  print("[!] ExceptionStatus")
