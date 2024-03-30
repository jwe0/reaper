import socket, os, json
from pystyle import Center, Colorate, Colors
from Utils.colors import RED, YELLOW, GREEN, BLUE, WHITE
from Api.layer4 import tcpflood, udpflood, synflood
from Api.layer7 import post, get, delete, patch
from Api.tools import reversedns, portscan, socketserverdebug, apidebugger

class Utils:
    def clear():
        os.system("cls") if os.name == "nt" else os.system("clear")


    def art():
        Utils.clear()
        art = """



    ____                            
   / __ \___  ____ _____  ___  _____
  / /_/ / _ \/ __ `/ __ \/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ /  __/ /    
/_/ |_|\___/\__,_/ .___/\___/_/ v1
                /_/                 
        """
        print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(art)))


    def title(data):
        if data == None:
            os.system("title Reaper Stresser")
        else:
            os.system("title Reaper Stresser {}".format(data))



class Menus:
    def Layer_4():
        Utils.title("[~] Layer 4")
        Utils.art()
        options = """
[ 1 ] ~ (TCP)
[ 2 ] ~ (UDP)
[ 3 ] ~ (SYN)
        """
        print(Center.XCenter(options))
        mode = input("mode : ")
        target = input("target : ")
        port = input("port : ")
        packet_size = input("packet size : ")

        match mode:
            case "1":
                Utils.title(f"[~] Layer 4 [~] TCP [~] {target}")
                tcpflood(target, int(port), int(packet_size))
            case "2":
                Utils.title(f"[~] Layer 4 [~] UDP [~] {target}")
                udpflood(target, int(port), int(packet_size))
            case "3":
                Utils.title(f"[~] Layer 4 [~] SYN [~] {target}")
                synflood(target, int(port), int(packet_size))


    def Layer_7():
        Utils.title("[~] Layer 7")
        Utils.art()
        options = """
[ 1 ] ~ (POST)
[ 2 ] ~ (GET)
[ 3 ] ~ (PATCH)
[ 4 ] ~ (DELETE)
        """
        print(Center.XCenter(options))
        mode = input("mode : ")
        target = input("target : ")
        code = input("success code : ")
        match mode:
            case "1":
                Utils.title(f"[~] Layer 7 [~] POST [~] {target}")
                post(target, int(code))
            case "2":
                Utils.title(f"[~] Layer 7 [~] GET [~] {target}")
                get(target, int(code))
            case "3":
                Utils.title(f"[~] Layer 7 [~] PATCH [~] {target}")
                patch(target, int(code))
            case "4":
                Utils.title(f"[~] Layer 7 [~] DELETE [~] {target}")
                delete(target, int(port))


    def Tools():
        Utils.title("[~] Tools/Debuggers")
        Utils.art()
        options = """
[ 1 ] ~ (Reverse DNS)
[ 2 ] ~ (Port scan)
[ 3 ] ~ (Sock debug)
[ 4 ] ~ (Api debug)
        """
        print(Center.XCenter(options))
        mode = input("mode : ")
        target = input("target: ")
        match mode:
            case "1":
                Utils.title(f"[~] Tools [~] REVERSE DNS [~] {target}")
                reversedns(target)
            case "2":
                Utils.title(f"[~] Tools [~] PORT SCANNER [~] {target}")
                portscan(target)
            case "3":
                Utils.title(f"[~] Tools [~] SOCKET DEBUGGER [~] {target}")
                port = input("port : ")
                socketserverdebug(target, int(port))
            case "4":
                Utils.title(f"[~] Tools [~] API DEBUGGER [~] {target}")
                method = input("method : ")
                headers = input("headers : ")
                data = input("json data : ")
                headers = json.loads(headers)
                json_data = json.loads(data)

                apidebugger(target, json_data, headers, method)




class Main:
    def Main():
        Utils.title("[~] Hub")
        Utils.art()
        options = """
[ 1 ] ~ (Layer 4)
[ 2 ] ~ (Layer 7) 
[ 3 ] ~ (Tools)
        
        """
        print(Center.XCenter(options))

        choose = input(": ")

        match choose:
            case "1":
                Menus.Layer_4()
            case "2":
                Menus.Layer_7()
            case "3":
                Menus.Tools()





if __name__ == "__main__":
    while True:
        Main.Main()