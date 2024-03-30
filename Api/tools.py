import socket, requests, random

def agent():
    with open("Dependencies/Agents.txt") as f:
        return random.choice([agent for agent in f.read().splitlines()])

def reversedns(target):
    data = socket.gethostbyname(target)
    print(f"[+] The IP of {target} is {data}")
    input()

def portscan(target):
    ports = [80, 8080, 8000, 443, 22, 21]

    port_info = {
        "80" : "Standard http port",
        "8080" : "Secondary http proxy",
        "443" : "Https port",
        "22" : "SSH service",
        "21" : "FTP service"
    }


    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        con = s.connect_ex((target, port))
        if con == 0:
            data = port_info.get(str(port))
            print("(+) Port {} is open | {info}".format(str(port), info=data))

    input("[+] Finished scan press enter to exit.")


def socketserverdebug(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    con = s.connect_ex((target, port))

    if con == 0:
        print("Connected to server")
        
        try:
            response = s.recv(1024).decode()
            print(f"[{str(target)}:{str(port)}] Response: {response}")
        except:
            print(f"[{str(target)}:{str(port)}] NO RESPONSE")
        while True:
            addr, adp = s.getsockname()
            message = input(f"[REAPER:{str(adp)}] message : ")
            if message.lower() == "exit":
                
                input("[+] Closed connection and broke loop. Press enter to close")
                s.close()
                break
                

            s.send(message.encode())
            try:
                response = s.recv(1024).decode()
                print(f"[{str(target)}:{str(port)}] Response: {response}")
            except:
                print(f"[{str(target)}:{str(port)}] NO RESPONSE")
                continue



def apidebugger(target, data, headers, method):
    if method == "get":
        headers["User-Agent"] = agent()

        if data:
            con = requests.get(target, json=data, headers=headers)
        else:
            con = requests.get(target, headers=headers)

        try:
            print(f"[{target}] Status: {con.status_code}\nData: {json.dumps(con.text, indent-4)}")
        except:
            print(f"[{target}] Status: {con.status_code} | Data: {con.text}")
        input()

    elif method == "post":
        headers["User-Agent"] = agent()

        if data:
            con = requests.post(target, json=data, headers=headers)
        else:
            con = requests.post(target, headers=headers)

        try:
            print(f"[{target}] Status: {con.status_code}\nData: {json.dumps(con.text, indent-4)}")
        except:
            print(f"[{target}] Status: {con.status_code} | Data: {con.text}")
        input()

    elif method == "put":
        headers["User-Agent"] = agent()

        if data:
            con = requests.put(target, json=data, headers=headers)
        else:
            con = requests.put(target, headers=headers)

        try:
            print(f"[{target}] Status: {con.status_code}\nData: {json.dumps(con.text, indent-4)}")
        except:
            print(f"[{target}] Status: {con.status_code} | Data: {con.text}")
        input()

    elif method == "delete":
        headers["User-Agent"] = agent()

        if data:
            con = requests.delete(target, json=data, headers=headers)
        else:
            con = requests.delete(target, headers=headers)

        try:
            print(f"[{target}] Status: {con.status_code}\nData: {json.dumps(con.text, indent-4)}")
        except:
            print(f"[{target}] Status: {con.status_code} | Data: {con.text}")
        input()

    elif method == "patch":
        headers["User-Agent"] = agent()

        if data:
            con = requests.patch(target, json=data, headers=headers)
        else:
            con = requests.patch(target, headers=headers)

        try:
            print(f"[{target}] Status: {con.status_code}\nData: {json.dumps(con.text, indent=4)}")
        except:
            print(f"[{target}] Status: {con.status_code} | Data: {con.text}")
        input()