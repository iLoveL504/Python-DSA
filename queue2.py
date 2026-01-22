from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("  ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")
        print('front before dequeue: ', numbers_queue.buffer)
        numbers_queue.dequeue()
        print('front: ', front)

if __name__ == '__main__':
    produce_binary_numbers(10)