class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)

        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None:
            return False

        if key == root.key:
            return True
        elif key < root.key:
            return self._search_recursive(root.left, key)
        else:
            return self._search_recursive(root.right, key)

    def pre_order_traversal(self):
        result = []
        self._pre_order_traversal_recursive(self.root, result)
        return result

    def _pre_order_traversal_recursive(self, root, result):
        if root is None:
            return

        result.append(root.key)
        self._pre_order_traversal_recursive(root.left, result)
        self._pre_order_traversal_recursive(root.right, result)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal_recursive(self.root, result)
        return result

    def _in_order_traversal_recursive(self, root, result):
        if root is None:
            return

        self._in_order_traversal_recursive(root.left, result)
        result.append(root.key)
        self._in_order_traversal_recursive(root.right, result)

    def post_order_traversal(self):
        result = []
        self._post_order_traversal_recursive(self.root, result)
        return result

    def _post_order_traversal_recursive(self, root, result):
        if root is None:
            return

        self._post_order_traversal_recursive(root.left, result)
        self._post_order_traversal_recursive(root.right, result)
        result.append(root.key)

    def level_order_traversal(self):
        result = []
        return self._level_order_traversal_recursive(self.root, result)

    def _level_order_traversal_recursive(self, root, result):
        if root is None:
            return

        queue = [root]
        while queue:
            node = queue.pop(0)
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, root):
        if root is None:
            return -1
        left_height = self._height_recursive(root.left)
        right_height = self._height_recursive(root.right)

        return max(left_height, right_height) + 1


bst = BinarySearchTree()
values = [50, 30, 20, 40, 70, 60, 80]
for value in values:
    bst.insert(value)

print("Pre-order traversal:", bst.pre_order_traversal())
print("In-order traversal:", bst.in_order_traversal())
print("Post-order traversal:", bst.post_order_traversal())
print("Level-order traversal:", bst.level_order_traversal())
print(bst.search(70))
print(bst.search(90))
print(bst.height())
