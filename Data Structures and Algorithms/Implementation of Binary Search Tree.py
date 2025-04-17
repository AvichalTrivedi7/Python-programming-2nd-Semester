class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        # Insert a new key into the BST
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        # Helper method to insert recursively
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)
        # If key == current_node.key, do nothing (no duplicates)

    def pre_order(self, node):
        # Pre-order traversal: root, left, right
        if node:
            print(node.key, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        # In-order traversal: left, root, right
        if node:
            self.in_order(node.left)
            print(node.key, end=' ')
            self.in_order(node.right)

    def post_order(self, node):
        # Post-order traversal: left, right, root
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.key, end=' ')

    def count_nodes(self, node):
        # Count total nodes in the BST recursively
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Pre-order Traversal:")
bst.pre_order(bst.root)  
print("\nIn-order Traversal:")
bst.in_order(bst.root) 
print("\nPost-order Traversal:")
bst.post_order(bst.root) 

print("\nNumber of nodes in the BST:", bst.count_nodes(bst.root)) 
