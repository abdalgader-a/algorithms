"""
Description: Implementation of Queue using a Python list!
Complexity:
    enqueue is O(1)
    dequeue is O(1)
    peek is O(1)
"""


class QueueList(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def dequeue(self):
        return self.storage.pop(0)

    def peek(self):
        return self.storage[0]


# Test cases
q = QueueList(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())
print(q.dequeue())
