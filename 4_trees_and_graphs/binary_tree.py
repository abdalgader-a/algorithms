"""
Description: Implementation of the Binary Tree (preorder traversal).
Time complexity:
    search: O(n)
Space complexity: O(h), h is height of the tree

"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, value):
        return self.preorder_search(self.root, value)

    def print_tree(self):
        printed_tree = self.preorder_print(self.root)
        return printed_tree[:-1]

    def preorder_search(self, start, value):
        if value == start.value:
            return True
        else:
            if start.left is not None:
                return self.preorder_search(start.left, value)

            if start.right is not None:
                return self.preorder_search(start.right, value)
        return False

    def preorder_print(self, start):
        if start is None:
            return ""

        return str(start.value) + "-" + self.preorder_print(start.left) +\
            self.preorder_print(start.right)


# Test cases

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())
