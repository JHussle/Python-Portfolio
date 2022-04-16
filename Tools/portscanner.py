import socket
from queue import Queue
import threading

target = "XXX.XXX.XXX.XXX" # Target port that needs to be scanned

q = Queue()
for x in range(1, 501):
    q.put(x)
    
def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False
def worker():
    while True:
        port = q.get()
        if portscan(port):
            print("Port {} is open!")

        else:
            print("Port {} is closed!".format(x))

for x in range(30):
    t = threading.Thread(target=worker)
    t.start()