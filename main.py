import requests, re, random, string, threading, time


def randomstring():
  randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]
  return ''.join(randlst)


user = input("Username > ")
message = input("Message > ")
client = requests.Session()

data = {
  "theme_form[redirect_url]": "",
  "commit": "匿名で質問を送る"
}

def spam():
  global message
  r = client.get(f"https://www.ninjar.jp/users/{user}/themes/new")
  c = re.findall('"csrf-token" content=".+"', r.text)[0].split('"')[3]
  print("[+] Got Token: " + c)
  data["theme_form[title]"] = message+" - "+randomstring()
  data["authenticity_token"] = c
  r = client.post(f"https://www.ninjar.jp/users/{user}/themes",
                 data=data,
                 allow_redirects=True)
  if r.status_code == 200:
    print("[+] SendedMessage")
  else:
    print("[!] ExceptionStatus : " + r.status_code)
while True:
  threading.Thread(target=spam).start()
  time.sleep(0.5)
