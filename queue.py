import threading
import time
from collections import deque

orders = ['pizza','samosa','pasta','biryani','burger']


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[-1]
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def print(self):
        return list(self.buffer)

order_queue = Queue()

def place_order(*ord):
    for o in orders:
        # time.sleep(0.5)
        print('Order Placed!!: ', o)
        order_queue.enqueue(o)

def serve_order():
    while order_queue.size()!= 0:
        time.sleep(1)
        print('Order coming right up!: ', order_queue.dequeue())

# t1 = threading.Thread(target=place_order, args=(orders))
# t2 = threading.Thread(target=serve_order)
place_order(orders)
# t1.start()
# time.sleep(0.5)
# t2.start()

# Exercise no 2
# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,

print((list(range(1, 11))))

def binary_numbers():
    for number in range(1, 11):
        bn = Queue()

        while True:
            if number == 0:
                bn.enqueue('0')
                break
            if number == 1:
                bn.enqueue('1')
                break
            remainder = number%2
            if remainder == 1:
                bn.enqueue('1')
            else:
                bn.enqueue('0')
            number //= 2

        print(''.join(bn.print()))
binary_numbers()