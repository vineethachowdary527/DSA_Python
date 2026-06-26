#basic tree program
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)

inorder(root)
