import threading
import time

x = 8192

def halved():
    global x
    while(x > 1):
        x /= 2
        print(x)
        time.sleep(1)
    print("END!")
    
def double():
    global x
    while(x < 16384):
        x *= 2
        print(x)
        time.sleep(1)
    print("END!")

t1 = threading.Thread(target=halved)
t2 = threading.Thread(target=double)

t1.start()
t2.start()