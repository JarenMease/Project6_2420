class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node=None):
        if node is None:
            return 0

        left_size = self._size(node.left)
        right_size = self._size(node.right)

        return 1 + self._size(node.left) + self._size(node.right)

    def is_empty(self):
        return self.root is None

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1

        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return 1 + max(left_height, right_height)

    def add(self, key):
        self.root = self._add(self.root, key)
        return self

    def _add(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._add(node.left, key)
        else:
            node.right = self._add(node.right, key)
        return node

    def remove(self, key):
        self.root = self._remove(self.root, key)
        return self

    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.data:
            node.left = self._remove(node.left, key)
        elif key > node.data:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_value = self._min_value_node(node.right)
            node.data = min_value
            node.right = self._remove(node.right, min_value)
        return node

    def find(self, key):
        data = self._find(self.root, key)
        if data is None:
            raise ValueError(f"{key} not found in the tree")
        return data

    def _find(self, node, key):
        if node is None:
            return None
        if key == node.data:
            return node.data
        elif key < node.data:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.data)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.data)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print(node.data)
            self._print_tree(node.right)

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node.data

    def print_tree_structure(self):
        self._print_tree_structure(self.root)

    def _print_tree_structure(self, node):
        if node is not None:
            self._print_tree_structure(node.left)
            print(node.data)
            self._print_tree_structure(node.right)

