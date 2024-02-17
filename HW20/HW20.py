class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(value)

    def insert(self, index, value):
        if index < 0:
            raise IndexError("Negative index not allowed")

        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
                if current_node is None:
                    raise IndexError("Index out of range")
            new_node.next = current_node.next
            current_node.next = new_node

    def remove(self, value):
        if self.head is None:
            raise ValueError("Linkedlist is empty")
        
        if self.head.value == value:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next and current_node.next.value != value:
                current_node = current_node.next
            if current_node.next is None:
                raise ValueError("Value not found")
            current_node.next = current_node.next.next

    def remove_last(self):
        if self.head is None:
            raise ValueError("Linkedlist is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None

    def print_elements(self):
        current_node = self.head
        while current_node:
            if current_node.next:
                print(f"{current_node.value}", end=' -> ')
            else:
                print(f"{current_node.value}")
            current_node = current_node.next

# ================
linked_list_1 = LinkedList()

linked_list_1.append(80)
linked_list_1.append(25)
linked_list_1.append(49)
linked_list_1.append(21)
linked_list_1.append(19)
linked_list_1.append(89)
linked_list_1.append(31)

linked_list_1.insert(5, 160)
linked_list_1.insert(5, 200)

linked_list_1.print_elements()

linked_list_1.remove(160)
linked_list_1.remove(200)
linked_list_1.print_elements()

linked_list_1.remove_last()
linked_list_1.print_elements()

#=============
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from an empty stack")
        
# ==========
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.pop()) 
print(my_stack.pop()) 
print(my_stack.pop())  
print(my_stack.is_empty())  