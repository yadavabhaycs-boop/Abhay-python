import threading 
class Mythread(threading.Thread):
    def run(self):
        print("Thread is running")
    
t = Mythread() 
t.start() 
t.join() 

