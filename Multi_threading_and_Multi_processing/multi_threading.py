import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number {i}")


def print_Letter():
    for i in "abcde":
        time.sleep(2)
        print(f"Letter {i}")

#create thread
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_Letter)


t = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
f_time = time.time() - t
print(f_time)