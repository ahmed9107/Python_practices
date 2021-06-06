# ---------------------
# ---- Ahmed Azami ----
# ---------------------
# ---- Linked List ----
# ---------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.reference = None

class LinkedList:

    def __init__(self):
        self.head = None

    # Next Linked List Items
    def next(self):
        if self.head is None:
            print("The List is empty!")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data , end=" ")
                n = n.reference

    # Inserting Items at the Beginning
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.reference = self.head
        self.head = new_node

    # Inserting Items at the End
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.reference is not None:
            n= n.reference
        n.reference = new_node

    # Inserting Item after another Item
    def insert_after_item(self, x, data):
        n = self.head
        print(n.reference)
        while n is not None:
            if n.data == x:
                break
            n = n.reference
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.reference = n.reference
            n.reference = new_node

    # Inserting Item before another Item
    def insert_before_item(self, x, data):
        if self.head is None:
            print("List has no element")
            return
        if x == self.head.data:
            new_node = Node(data)
            new_node.reference = self.head
            self.head = new_node
            return
        n = self.head
        print(n.reference)
        while n.reference is not None:
            if n.reference.data == x:
                break
            n = n.reference
        if n.reference is None:
            print("Item not in the list")
        else:
            new_node = Node(data)
            new_node.reference = n.reference
            n.reference = new_node

    # Inserting Data at Specific Index
    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.reference = self.head
            self.head = new_node
        i = 1
        n = self.head
        while i < index-1 and n is not None:
            n = n.reference
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.reference = n.reference
            n.reference = new_node

    # Function to counts the total number of elements.
    def length(self):
        if self.head is None:
            return 0
        n = self.head
        m = 0
        while n is not None:
            m = m + 1
            n = n.reference
        return m



new_linked_list = LinkedList()

new_linked_list.insert_at_end(1)
new_linked_list.insert_at_end(2)
new_linked_list.insert_at_end(3)
new_linked_list.insert_at_end(4)
new_linked_list.insert_at_end(5)

# New List: 1 2 3 4 5
new_linked_list.next()
print('-' * 1)
print('-' * 50)

# New List: 6 1 2 3 4 5
new_linked_list.insert_at_start(6)
new_linked_list.next()
print('-' * 1)
print('-' * 50)

# New List: 6 1 2 3 4 7 5
new_linked_list.insert_after_item(4, 7)
new_linked_list.next()
print('-' * 1)
print('-' * 50)

# New List: 6 1 2 8 3 4 7 5
new_linked_list.insert_before_item(3, 8)
new_linked_list.next()
print('-' * 1)
print('-' * 50)

# New List: 6 1 9 2 8 3 4 7 5
new_linked_list.insert_at_index(3, 9)
new_linked_list.next()
print('-' * 1)
print('-' * 50)

print("Length of the linked list is: " + str(new_linked_list.length()))

