import threading


from random import randint
from time import sleep


def foo(name):
    print(f"I'm {name} and I started work")
    sleep(randint(1, 8))
    print(f"I'm {name} and I stopped working")


t1 = threading.Thread(target=foo, args=("w1",))
t2 = threading.Thread(target=foo, args=("w2",))
t3 = threading.Thread(target=foo, args=("w3",))
t4 = threading.Thread(target=foo, args=("w4",))
t5 = threading.Thread(target=foo, args=("w5",))


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
print("=====")

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
print('KONIEC')