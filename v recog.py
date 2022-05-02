import threading
import time

def demo():
    print("welcome")

t=threading.Timer(3,demo)
t.start()