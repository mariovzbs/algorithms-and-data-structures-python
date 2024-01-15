class TreeNode:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if node is None:
            return
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return TreeNode(data)

        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)

        self._update_height(root)
        balance = self._balance_factor(root)
        print("NODE", root.data)
        print("BALANCE", balance)
        if balance > 1 and data < root.left.data:
            print("BALANCING LL")
            return self._rotate_left(root)

        return root


avl = AVLTree()
values = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for value in values:
    avl.insert(value)
