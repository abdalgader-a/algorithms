"""
Description: Implementation of the Stack using LinkedList
Time complexity:
    insert_first is O(1)
    delete_first is O(1)

Space complexity is O(1)
"""

from linkedlist import *


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_first(self, new_element) -> None:
        """Insert new element as head of the linkedList"""
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """Delete the first element (head) of the linkedList"""
        if self.head:
            current = self.head
            temp = current
            self.head = current.next
            return temp
        else:
            return None


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, el) -> None:
        self.ll.insert_first(el)

    def pop(self) -> Element:
        return self.ll.delete_first()


# Test cases
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)

stack = Stack(e1)

stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)

