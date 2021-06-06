class stack:
    def __init__(self):
        self.items = []
    def push(self, data):
        # Push element in the items list
        self.items.append(data)
        return True
    def pop(self):
        # Check if items list is empty if not pop the last element added in the list
        if len(self.items) == 0:
            return "The stack is empty"
        else:
            return self.items.pop()
    def print_stack(self):
        print(self.items)

# Example:

my_stack = stack()

my_stack.push("Mon")
my_stack.push("Tue")
my_stack.push("Wed")
my_stack.push("Thu")
my_stack.push("Fri")
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()

# Output: ["Mon"]
my_stack.print_stack()






