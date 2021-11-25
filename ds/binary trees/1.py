
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

'''
Algorithm Inorder(tree)
   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   2. Visit the root.
   3. Traverse the right subtree, i.e., call Inorder(right-subtree)
Uses of Inorder '''

def PrintInorder(root):
    if root:
        PrintInorder(root.left)
        print(root.val)
        print(root.right)



'''
Algorithm Preorder(tree)
   1. Visit the root.
   2. Traverse the left subtree, i.e., call Preorder(left-subtree)
   3. Traverse the right subtree, i.e., call Preorder(right-subtree) 


'''

def PrintPreorder(root):
    if root:
        print(root.val)
        print(root.left)
        print(root.right)

'''
Algorithm Postorder(tree)
   1. Traverse the left subtree, i.e., call Postorder(left-subtree)
   2. Traverse the right subtree, i.e., call Postorder(right-subtree)
   3. Visit the root.

'''

def PrintPostorder(root):
    if root:
        print(root.left)
        print(root.right)
        print(root.val)







root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left = Node(4)

PrintPostorder(root)