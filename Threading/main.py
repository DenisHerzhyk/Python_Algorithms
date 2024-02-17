# 3.1 GIL

# 3.1.1 test

import threading
import time


def counter1():
    for i in range(1, 1000001):
        pass


def counter2():
    for i in range(1000001, 2000001):
        pass


start_time = time.time()

t1 = threading.Thread(target=counter1)
t2 = threading.Thread(target=counter2)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()
total_time = end_time - start_time

print(f"Total time: {total_time}")


# 3.1.2 test

def counter():
    for i in range(1, 2000001):
        pass


start_time = time.time()

t = threading.Thread(target=counter)
t.start()
t.join()

end_time = time.time()
total_time = end_time - start_time

print(f"Total time: {total_time}")


# 3.2

# 3.2.1 test

def sum():
    sum = 0
    for i in range(1, 1000001):
        sum += i


def mult():
    mult = 1
    for i in range(1, 1000):
        mult *= i


start_time = time.time()

t1 = threading.Thread(target=sum)
t2 = threading.Thread(target=mult)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()
total_time = end_time - start_time

print(f"Total time: {total_time}")


# 3.2.2 test
def oper():
    sum = 0
    mult = 1
    for i in range(1, 1001):
        mult *= i
    for i in range(1, 1000001):
        sum += i

    print(sum)
    print(mult)


start_time = time.time()

t = threading.Thread(target=oper)
t.start()
t.join()

end_time = time.time()
total_time = end_time - start_time

print(f"Total time: {total_time}")
