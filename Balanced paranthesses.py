# ----------------------------
# -- Created By Ahmed Azami --
# ----------------------------
# --- Balanced parentheses ---
# ----------------------------

class stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, data):
        # Push element in the items list
        self.items.append(data)
        return True
    def pop(self):
        return self.items.pop()
    def stack_items(self):
        return self.items

# Function to check if the open and the close parentheses are the same
def Pair(Open, Close):
    if Open == '(' and Close == ')':
        return True
    elif Open == '{' and Close == '}':
        return True
    elif Open == '[' and Close == ']':
        return True
    else:
        return False

def balanced_Parentheses(expression):
    s = stack()
    for i in expression:
        if i == '(' or i == '{' or i == '[':
            s.push(i)
        if i == ')' or i == '}' or i == ']':
            if s.is_empty():
                return False
            elif Pair(s.items[-1], i) == False:
                return False
            else:
                s.pop()

    # Check if the stack is empty or not
    if s.is_empty():
        return True
    else:
        return False

# Write an expression with any parentheses
print(balanced_Parentheses(input()))
