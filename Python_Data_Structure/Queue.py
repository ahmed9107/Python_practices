# -------------------
# --- Ahmed Azami ---
# -------------------

class queue:
    def __init__(self):
        self.items = []

    # Add element in the items list
    def enqueue(self, data):
        self.items.insert(0, data)
    
    # Check if items list is empty if not remove the first element added in the list
    def dequeue(self):
        if len(self.items) == 0:
            return 'The Queue is empty'
        else:
            return self.items.pop()

    # Print items list
    def print_queue(self):
        for item in self.items:
            print(self.items)


# Example:
My_Queue = queue()

My_Queue.enqueue(1)
My_Queue.enqueue(9)
My_Queue.enqueue(8)
My_Queue.enqueue(5)
My_Queue.enqueue(4)
My_Queue.dequeue()
My_Queue.dequeue()
My_Queue.dequeue()
My_Queue.dequeue()

# Output = 4
My_Queue.print_queue()