import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = 'ip here'

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port,'is open!!')

        con.close()

    except:
        pass

def threader():
    while True:
        workrt =q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,65535):
    q.put(worker)

q.join()
