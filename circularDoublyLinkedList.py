# circularDoublyLinkedList.py

class Node:
    def __init__(self, data):
        self.data = data  # data는 (이름, 생일)
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def __iter__(self):
        node = self.head
        if not node:
            return
        yield node.data
        node = node.next
        while node != self.head:
            yield node.data
            node = node.next
