import threading
def greet():
    print("Hii from Thread!")
t = threading.Thread(target=greet)
t.start()
t.join()
