import requests, time


def on_ready():
    print("------------")
    print("Made by leoidagoat on discord")
    print("this is free-to-use.")
    print("------------")
    start()

def start():
    while True:
        cookie = input(str("enter a cookie: "))
        cookies = {
            ".ROBLOSECURITY": cookie
            }
        resdatauser = requests.get("https://users.roblox.com/v1/users/authenticated", cookies=cookies)
        if resdatauser.status_code == 200:
            datauserjson = resdatauser.json()
            print("- user lookup success!")
            robuxuserres = requests.get(f"https://economy.roblox.com/v1/users/{datauserjson['id']}/currency", cookies=cookies)
            if robuxuserres.status_code == 200:
                robuxuserresdata = robuxuserres.json()
                print("- robux lookup success!")
                print("$ ------------- $")
                print("- Basic data: ")
                print(f"   username: {datauserjson['name']}")
                print(f"   displayName: {datauserjson['displayName']}")
                print(f"   userid: {datauserjson['id']}")
                print("- Balance data: ")
                print(f"   Balance: {robuxuserresdata['robux']}")
                time.sleep(5)
                start()
            else:
                print("- failed to get robux balance!")
                start()
        else:
            print("cookie is invaild!")
            start()
if __name__ == "__main__":
    on_ready()
