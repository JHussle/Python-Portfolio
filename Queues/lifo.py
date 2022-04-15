import queue

q = queue.LifoQueue()

number = [1, 2, 3, 4, 5, 6, 7, 8]

for x in number:
    q.put(x)

while not q.empty():
    print(q.get())