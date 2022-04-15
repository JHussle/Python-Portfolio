import socket

target = "192.168.1.252"

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False
for x in range(1, 501):
    if(portscan(x)):
        print("Port {} is open!".format(x))
    else:
        print("Port {} is closed!".format(x))