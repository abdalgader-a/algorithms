"""

Description: Implementation of the Binary Search Tree.

Time complexity:
    search: O(n)
Space complexity: O(h), h is height of the tree

"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_value):
        return self.insert_operation(self.root, new_value)

    def insert_operation(self, current, new_value):
        if new_value < current.value:
            if current.left:
                self.insert_operation(current.left, new_value)
            else:
                current.left = Node(new_value)
        else:
            if current.right:
                self.insert_operation(current.right, new_value)
            else:
                current.right = Node(new_value)

    def search(self, value):
        return self.search_operation(self.root, value)

    def search_operation(self, current, value):
        if current:
            if value == current.value:
                return True
            elif value < current.value:
                return self.search_operation(current.left, value)
            else:
                return self.search_operation(current.right, value)
        else:
            return False


# Test cases
tree = BinarySearchTree(5)

tree.insert(3)
tree.insert(8)
tree.insert(1)
tree.insert(10)

print(tree.search(1))
tree.insert(7)
tree.insert(2)
print(tree.search(6))
