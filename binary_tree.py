class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def insert_left(self, node, data):
        new_node = TreeNode(data)
        if node.left is None:
            node.left = new_node
        else:
            new_node.left = node.left
            node.left = new_node
        return node

    def insert_right(self, node, data):
        new_node = TreeNode(data)
        if node.right is None:
            node.right = new_node
        else:
            new_node.right = node.right
            node.right = new_node
        return node


tree = BinaryTree("A")
tree.insert_left(tree.root, "B")
tree.insert_right(tree.root, "C")
tree.insert_left(tree.root.left, "D")
tree.insert_right(tree.root.left, "E")
print(tree.root.data, end="<")
print(tree.root.left.data, end="<")
print(tree.root.right.data, end="<")
print(tree.root.left.left.data, end="<")
print(tree.root.left.right.data)
