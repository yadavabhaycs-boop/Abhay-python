import threading 
def task():
    for i in range(3):
        print(f"Task running: {i}")
        
t = threading.Thread(target=task) 
t.start() 
t.join() 
