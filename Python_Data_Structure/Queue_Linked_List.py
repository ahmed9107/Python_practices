# -----------------------
# ----- Ahmed Azami -----
# -----------------------
# -- Queue Linked List --
# -----------------------

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue_Linked_List:
    def __init__(self, front=None, tail=None):
        self.front = front
        self.tail = tail

    def isEmpty(self):
        if self.front is None and self.tail is None:
            return True
        else:
            return False

    def enqueue(self, data):
        newNode = Node(data)
        newNode.next_node = None
        if self.isEmpty():
            self.front = self.tail = newNode
        else:
            self.tail.next_node = newNode
            self.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return
        else:
            if self.front == self.tail:
                self.front = self.tail = None
            else:
                self.front = self.front.next_node

    def front_value(self):
        if self.isEmpty():
            raise ValueError('Linked List is empty')
        else:
            return self.front.data


obj = Queue_Linked_List()

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)

while not obj.isEmpty():
    print(obj.front_value())
    obj.dequeue()
