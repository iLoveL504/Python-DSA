# Linked Lists

class Node:
    def __init__ (self, data=None, next=None):
        self.data = data
        self.next = next
     

class LinkedList:
    def __init__ (self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        return count
    
    def remove_at(self, index):
        if index < 0 or index >=self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                current.next = current.next.next
                break
            current = current.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        current = self.head
        while current:
            print(current.data)   
            if count == index:
                node = Node(data, current.next)
                print('current data: ', current.data)
                print('node data: ', node.data)
                print('current node data: ', current.data)
                print('current next data: ', current.next.data)
                current.next = node

                break
            print('count: ', count)
            current = current.next
            count += 1

    
    def print(self):
        if self.head is None:
            print("list is empty")
            return
        
        current = self.head
        list = []

        while current:
            list.append(str(current.data))
            current = current.next

        print(' -> '.join(list))

ll = LinkedList()
ll.insert_values([54, 73, 14, 66])
ll.remove_at(1)
ll.insert_at(1, 73)
ll.print()

