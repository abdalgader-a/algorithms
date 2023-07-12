"""
Description: Implementation of the queue using LinkedList
Time complexity:
    insert_first is O(1)
    delete_first is O(1)

Space complexity is O(1)
"""
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_last(self, new_element) -> None:
        """Insert new element as end of the linkedList"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
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


class Queue(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def enqueue(self, el) -> None:
        self.ll.insert_last(el)

    def dequeue(self) -> Element:
        return self.ll.delete_first()


# Test cases
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)

q = Queue(e1)
q.enqueue(e2)
q.enqueue(e3)

# Should be 1
print(q.dequeue().value)
e4 = Element(4)
q.enqueue(e4)
# Should be 2
print(q.dequeue().value)
# Should be 3
print(q.dequeue().value)
# Should be 4
print(q.dequeue().value)

# Should be None
print(q.dequeue())

