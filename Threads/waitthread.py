import threading

def function():
    for x in range(200):
        print("Hello, World!")
        
t1 = threading.Thread(target=function)
t1.start()

t1.join(5)

print("THIS IS THE END!")