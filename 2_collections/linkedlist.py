"""
Description: Implementation of the LinkedList with three methods
        -"get_position" returns the element at a certain position.
        -"insert" function will add an element to a particular.
        -"delete" delete the first element with that particular value.
Time complexity:
    get_position is O(n)
    insert is O(n)
    delete is O(n)
Space complexity is O(1)
"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        if position <= 0:
            return "Invalid entry"

        current = self.head
        current_position = 1
        while current_position < position:
            current = current.next
            current_position += 1
        if current is None:
            return None
        else:
            return current

    def insert_elem(self, new_element, position):
        if position <= 0:
            return "Invalid entry"

        current = self.head
        while (position - 1) > 1:
            current = current.next
            position -= 1
        new_element.next = current.next
        current.next = new_element

    def delete_elem(self, value):
        current = self.head
        prev_elem = None
        if current.value == value:
            self.head = current.next
        else:
            while current.value != value:
                prev_elem = current
                current = current.next
            prev_elem.next = current.next

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


# Test cases
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)

ll = LinkedList(e1)
ll.append(e2)
print(ll.get_position(3).value)
ll.insert_elem(e3, 2)
ll.delete_elem(1)
