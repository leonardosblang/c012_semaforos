# importing the modules
from threading import *
import time

obj = Semaphore(2)


def display_semaphore(name):
    obj.acquire()
    for i in range(5):
        time.sleep(1)
        print("\n" + name)

        obj.release()


def display_no_semaphore(name):
    for i in range(5):
        time.sleep(1)
        print("\n" + name)


def start_thread():
    t1 = Thread(target=display_semaphore, args=('Thread 1',))
    t2 = Thread(target=display_semaphore, args=('Thread 2',))
    t3 = Thread(target=display_semaphore, args=('Thread 3',))
    t4 = Thread(target=display_semaphore, args=('Thread 4',))
    t5 = Thread(target=display_semaphore, args=('Thread 5',))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()


def start_thread_no_semaphore():
    t1 = Thread(target=display_no_semaphore, args=('Thread 1',))
    t2 = Thread(target=display_no_semaphore, args=('Thread 2',))
    t3 = Thread(target=display_no_semaphore, args=('Thread 3',))
    t4 = Thread(target=display_no_semaphore, args=('Thread 4',))
    t5 = Thread(target=display_no_semaphore, args=('Thread 5',))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()


start_function = input("Do you want to use the semaphore or not? (y/n)")
if start_function == "y":
    start_thread()
else:
    start_thread_no_semaphore()

