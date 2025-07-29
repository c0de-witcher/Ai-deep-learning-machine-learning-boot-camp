import multiprocessing
import time

def print_number():
    for i in range(5):
        time.sleep(1)
        print(f"Number {i}")

def print_letter():
    for i in "abcde":
        time.sleep(1)
        print(f"Letter {i}")

if __name__ == "__main__":
    # Create processes
    p1 = multiprocessing.Process(target = print_number)
    p2 = multiprocessing.Process(target = print_letter)

    t= time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    f_time = time.time()-t
    print(f_time)